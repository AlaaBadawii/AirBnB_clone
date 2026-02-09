#!/usr/bin/python3
"""Defines the HBNBCommand class for the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains:
    the entry point of the command interpreter"""
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User
        }

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[arg]()
            print(obj.id)
            obj.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        args = arg.split()
        result = []

        if args:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            objs = storage.all()
            for key, obj in objs.items():
                if key.split('.')[0] == args[0]:
                    result.append(str(obj))
        else:
            objs = storage.all()
            for _, obj in objs.items():
                result.append(str(obj))

        print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        elif args[2] in ("id", "updated_at", "created_at"):
            return
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()[key]
            setattr(obj, args[2], args[3])
            storage.save()

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
