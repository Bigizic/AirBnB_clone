#!/usr/bin/python3
"""contains the entry point of
the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """Representation of HBNBCommand console
    Attributes:
        prompt (string): the command prompt.
    """
    prompt = "(hbnb) "

    created_model = None
    created_id = None
    models = ["BaseModel", "User", "Place", "State", "City",
              "Amenity", "Review"]

    def default(self, arg):
        """Handle advanced cases
            Usage:
                <class_name>.all(): User.all(), Place.all()
                <class_name>.count(): User.count(), BaseModel.count()
                <class_name>.show(<id): User.show("my_id")
                <class_name>.destroy(<id>): User.destroy("my_id")
        """
        classes = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
        }
        cmd = arg.strip()

        if cmd.endswith(".all()"):
            class_name = cmd.split(".")[0]
            if class_name in self.models:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        elif cmd.endswith(".count()"):
            class_name = cmd.split(".")[0]
            if class_name in self.models:
                self.do_count(class_name)
            else:
                print("** class doesn't exist **")
        elif cmd.count("(") == 1 and cmd.endswith(")"):
            parts = cmd.split("(")
            class_id = parts[1][:-1].strip().strip('"')
            class_name, obj_id = parts[0].split(".", 1)
            if class_name in self.models:
                if obj_id == 'show':
                    self.do_show(class_name + " " + class_id)
                elif obj_id == 'destroy':
                    self.do_destroy(class_name + " " + class_id)
            else:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit is command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF is command to exit the program"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new class instance and prints it's id.
        """
        if arg:
            if arg in self.models:
                model_class = globals()[arg]
                new_instance = model_class()
                self.created_model = new_instance
                self.created_id = new_instance.id
                storage.save()
                storage.reload()
                print(self.created_id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Prints the string representation of a class given it's class name
        and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.models:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            input_id = args[1]
            instances = storage.all()

            found_instance = None
            for instance_dict in instances.values():
                if input_id == getattr(instance_dict, 'id', None):
                    found_instance = instance_dict
                    break
            if found_instance:
                print(found_instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes an instance based on the class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.models:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            input_id = args[1]
            instances = storage.all()

            found_instance = None
            for key, instance_dict in instances.items():
                if input_id == getattr(instance_dict, 'id', None):
                    found_instance = key
                    break

            if found_instance:
                del instances[found_instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Prints all string representation of all instances given class or not
        """
        instances = storage.all()
        output = []

        if len(arg) == 0:
            for instance in instances.values():
                output.append(str(instance))
            print(json.dumps(output))
        if len(arg) > 0:
            if arg in self.models:
                for instance in instances.values():
                    if arg == instance.__class__.__name__:
                        output.append(str(instance))
                print(json.dumps(output))
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute> <value>
        Updates an instance based on the class, id, attribute and value
        """
        args = arg.split()
        instances = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in self.models:
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False

        if len(args) == 2:
            found_id = False
            for key, instance_dict in instances.items():
                if args[1] == getattr(instance_dict, 'id', None):
                    found_id = True
                    break
            try:
                for elements in args[1]:
                    if type(eval(elements)) is int and not found_id:
                        print("** no instance found **")
                        return False
            except Exception:
                if isinstance(args[1], str) and not found_id:
                    print("** attribute name missing **")
                    return False
            if found_id:
                print("** attribute name missing **")
                return False

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        attr_name = args[2]
        attr_value = args[3].strip("\"'")

        if len(args) >= 4:
            ins_key = "{}.{}".format(args[0], args[1])
            if ins_key in instances:
                ins = instances[ins_key]
                if attr_name not in ['id', 'created_at', 'updated_at']:
                    setattr(ins, attr_name, attr_value)
                    storage.save()
                else:
                    return

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Prints the number of occurence of a class
        """
        count = 0
        instances = storage.all()

        if arg in self.models:
            for ins in instances.values():
                if arg == ins.__class__.__name__:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    """def default(self, arg):
        dict_of_commands = {
                "EOF": self.do_EOF,
                "quit": self.do_quit
                }
        search = re."""
