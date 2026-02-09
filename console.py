#!/usr/bin/python3
"""Defines the HBNBCommand class for the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains:
    the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_help(self, arg):
        """return a list of available cmds or what a specific cmd do  """
        return super().do_help(arg)

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """quit the program if EOF reached"""
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
