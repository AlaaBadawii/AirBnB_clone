#!/usr/bin/python3
"""Defines the HBNBCommand class for the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains:
    the entry point of the command interpreter"""
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State,
        "Place": Place
        }

    def do_create(self, arg):
        """Creates a new instance"""
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

    def do_count(self, arg):
        """return count of instances in a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg:
                    count += 1
            print(count)

    def default(self, line):
        """Handle the default case when an unrecognized command is entered."""
        if '.' in line and '(' in line and ')' in line:
            class_name = line[:line.find('.')]
            method = line[line.find('.') + 1:line.find('(')]

            if method == "all":
                return self.do_all(class_name)
            elif method == "count":
                return self.do_count(class_name)
            elif method == "show":
                id = line[line.find('(')+1:line.find(')')]
                id = id.strip('"')  # remove quotes if present
                return self.do_show(class_name + " " + id)
            elif method == "destroy":
                id = line[line.find('(')+1:line.find(')')]
                id = id.strip('"')  # remove quotes if present
                return self.do_destroy(class_name + " " + id)
            elif method == "update":
                args = line[line.find('(')+1:line.find(')')]

                args = args.replace(",", "")
                args = args.replace('"', "")

                return self.do_update(f"{class_name} {args}")

        print("*** Unknown syntax:", line)

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
