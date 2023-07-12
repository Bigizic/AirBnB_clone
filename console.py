#!/usr/bin/python3
"""contains the entry point of
the command interpreter"""


import cmd
from models.base_model import BaseModel
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
    models = ["BaseModel"]

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
        """Creates a new instance of BaseModel
        """
        if arg:
            if arg in self.models:
                new_instance = BaseModel()
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
        """Prints the string representation of an insance based
            on the class name and id
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
                instance = instance_dict
                if input_id == instance['id']:
                    found_instance = instance_dict
                    break
            if found_instance:
                print(BaseModel(**found_instance))
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id, Also
            saves the changes into the JSON file
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
                if input_id == instance_dict['id']:
                    found_instance = key
                    break

            if found_instance:
                del instances[found_instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
            or not on the class name example: all BaseModel or all
        """
        instances = storage.all()
        output = []
        if arg in self.models or len(arg) == 0:
            for instance in instances.values():
                output.append(str(BaseModel(**instance)))
            print(json.dumps(output))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
            adding or updating attribute example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com".
            Usage: <class name> <id> <attribute name> <attribute value>
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

        if "{}.()".format(args[0], args[1]) not in instances.keys():
            print("** no instance found **")
            return False

        if len(args) == 2:
            print("** attribute name missing **")
            return False

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            ins = instances["{}.{}".format(args[0], args[1])]
            if args[2] in ins.__class__.dict__.keys():
                my_type = type(obj.__class__.dict__[args[2]])
                ins.__dict__[args[2]] = my_type(args[3])
            else:
                ins.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            ins = instances["{}.{}".format(args[0], args[1])]
            for keys, values in eval(args[2]).items():
                if (keys in ins.__class__.__dict__.keys() and
                        type(ins.__class__.__dict__[keys]) in {
                            int, float, str}):
                    my_type = type(ins.__class__.__dict__[keys])
                    ins.__dict__[keys] = my_type(value)
                else:
                    ins.__dict__[keys] = value
        storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
    """def default(self, arg):
        dict_of_commands = {
                "EOF": self.do_EOF,
                "quit": self.do_quit
                }
        search = re."""
