#!/usr/bin/python3
"""The console module"""

from models.base_model import BaseModel
from models import storage
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """Console cmd class"""
    prompt = "(hbnb) "
    classess = ['BaseModel']

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

    def do_create(self, line):
        tmp = self.func(line, 1)
        if tmp:
            print(tmp)
        else:
            b = BaseModel()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Method to show instances"""
        tmp = self.func(line, 0)
        if tmp:
            print(tmp)
        else:
            tmp = line.split()
            key = "{}.{}".format(tmp[0], tmp[1])
            objs = storage.all()
            print(objs[key])

    def do_destroy(self, line):
        """Method to delete (destroy) an instance"""
        tmp = self.func(line, 0)
        if tmp:
            print(tmp)
        else:
            tmp = line.split()
            key = "{}.{}".format(tmp[0], tmp[1])
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
            tmp = line.split()
            _class = None
            try:
                _class = tmp[0]
            except IndexError:
                pass

            if _class and _class in self.classess:
                print(lst)
            else:
                print("** class doesn't exist **")

    def func(self, line, flag):
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

    def do_update(self, line):
        tmp = self.func(line, 0)
        if tmp:
            print(tmp)
        else:
            attrMsg = self.attrChecker(line)
            if attrMsg:
                print("{}".format(attrMsg))
            else:
                tmp = line.split()
                objs = storage.all()
                key = "{}.{}".format(tmp[0], tmp[1])
                if key in objs:
                    ins = objs[key]
                cast = self.valueCasting(tmp[3])
                if isinstance(cast, str):
                    cast = cast.strip('"')
                setattr(ins, tmp[2], cast)
                ins.save()

    def valueCasting(self, attrValue):
        intPattern = r'^-?[0-9]+$'
        floatPattern = r'^-?[0-9]*\.[0-9]+$'
        stringPattern = r'^.*$'

        typeFuncs = {1: int, 2: float, 3: str}
        patterns = [intPattern, floatPattern, stringPattern]
        count = 1
        for pat in patterns:
            if re.match(pat, attrValue) is not None:
                break
            count = count + 1
        return typeFuncs[count](attrValue)

    def attrChecker(self, line):
        tmp = line.split()
        attrName = None
        attrValue = None
        try:
            attrName = tmp[2]
            attrValue = tmp[3]
        except IndexError:
            pass
        if attrName is None:
            return "** attribute name missing **"
        elif attrValue is None:
            return "** value missing **"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
