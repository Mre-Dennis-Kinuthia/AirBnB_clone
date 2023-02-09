#!/usr/bin/env python

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_prompt(self, line):
        self.prompt = line + ": "

    def do_quit(self, s):
        """help quit

        Args:
            s (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

    def do_EOF(self, line):
        """help end of file

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

    def help(self):
        print("/n")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
