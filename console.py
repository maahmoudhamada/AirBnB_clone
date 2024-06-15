#!/usr/bin/python3
"""The console module"""

from models.base_model import BaseModel
from models import storage
import cmd


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
        if not line:
            print("** class name missing **")
        elif line not in self.classess:
            print("** class doesn't exist **")
        else:
            b = BaseModel()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Method to show instances"""
        tmp = line.split()
        _class = None
        id = None
        try:
            _class = tmp[0]
            id = tmp[1]
        except IndexError:
            pass
        if not line:
            print("** class name missing **")
        elif _class not in self.classess:
            print(_class)
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(_class, id)
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, line):
        """Method to delete (destroy) an instance"""
        tmp = line.split()
        _class = None
        id = None
        try:
            _class = tmp[0]
            id = tmp[1]
        except IndexError:
            pass
        if not line:
            print("** class name missing **")
        elif _class not in self.classess:
            print(_class)
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(_class, id)
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
            else:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
