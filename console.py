#!/usr/bin/python3
"""The console module"""

from models.base_model import BaseModel
from models.user import User
from models import storage
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """Console cmd class"""
    prompt = "(hbnb) "
    classess = ['BaseModel', 'User']

    def do_quit(self, line):
        """Exiting cmd loop"""
        return True

    def do_EOF(self, line):
        """Exiting cmd loop"""
        print()
        return True

    def emptyline(self):
        """Not exectuing anything"""
        pass

# ======================================================

    def argsChecker(self, line, flag):
        tmp = line.split()
        _class = None
        id = None
        try:
            _class = tmp[0]
            id = tmp[1]
        except IndexError:
            pass
        if not line:
            return "** class name missing **"
        elif _class not in self.classess:
            return "** class doesn't exist **"
        if flag != 1:
            if not id:
                return "** instance id missing **"
            else:
                key = "{}.{}".format(_class, id)
                objs = storage.all()
                if key not in objs:
                    return "** no instance found **"

# ======================================================

    def classSelector(self, inst):
        classess = [BaseModel, User]
        for _cls in classess:
            if inst == _cls.__name__:
                return _cls
        return None

# ======================================================

    def do_create(self, line):
        errorMssg = self.argsChecker(line, 1)
        if errorMssg:
            print(errorMssg)
        else:
            args = line.split()
            _cls = self.classSelector(args[0])
            inst = _cls()
            inst.save()
            print(inst.id)

    # ======================================================

    def do_show(self, line):
        """Method to show instances"""
        errorMssg = self.argsChecker(line, 0)
        if errorMssg:
            print(errorMssg)
        else:
            args = line.split()
            key = "{}.{}".format(args[0], args[1])
            objs = storage.all()
            print(objs[key])

    # ======================================================

    def do_destroy(self, line):
        """Method to delete (destroy) an instance"""
        errorMssg = self.argsChecker(line, 0)
        if errorMssg:
            print(errorMssg)
        else:
            args = line.split()
            key = "{}.{}".format(args[0], args[1])
            storage.all().pop(key)
            storage.save()

    def do_all(self, line):
        """Method to print all str repr of all objs"""
        objs = storage.all()
        lst = []
        for value in objs.values():
            lst.append(str(value))
        if not line:
            print(lst)
        else:
            args = line.split()
            _cls = None
            try:
                _cls = args[0]
            except IndexError:
                pass

            if _cls and _cls in self.classess:
                print(lst)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        errorMssg = self.argsChecker(line, 0)
        if errorMssg:
            print(errorMssg)
        else:
            attrMsg = self.attrChecker(line)
            if attrMsg:
                print("{}".format(attrMsg))
            else:
                args = line.split()
                objs = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in objs:
                    ins = objs[key]
                cast = self.valueCasting(args[3])
                if isinstance(cast, str):
                    cast = cast.strip('"')
                setattr(ins, args[2], cast)
                ins.save()

    def valueCasting(self, attrValue):
        intPattern = r'^-?[0-9]+$'
        floatPattern = r'^-?[0-9]*\.[0-9]+$'
        stringPattern = r'^.*$'

        typeargsCheckers = {1: int, 2: float, 3: str}
        patterns = [intPattern, floatPattern, stringPattern]
        count = 1
        for pat in patterns:
            if re.match(pat, attrValue) is not None:
                break
            count = count + 1
        return typeargsCheckers[count](attrValue)

    def attrChecker(self, line):
        args = line.split()
        attrName = None
        attrValue = None
        try:
            attrName = args[2]
            attrValue = args[3]
        except IndexError:
            pass
        if attrName is None:
            return "** attribute name missing **"
        elif attrValue is None:
            return "** value missing **"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
