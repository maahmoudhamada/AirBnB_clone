#!/usr/bin/python3
"""The console module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Console cmd class"""
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
