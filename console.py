#!/usr/bin/python3
"""contains the entry point of
the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Representation of HBNBCommand console
    Attributes:
        prompt (string): the command prompt.
    """
    prompt = "(hbnb) "

    created_model = BaseModel()
    created_id = created_model.id

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
            if arg in ["BaseModel"]:
                self.created_model.save()
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

        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            instance_id = args[1]
            if instance_id == self.created_id:
                print(self.created_model)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id, Also
            saves the changes into the JSON file
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            instance_id = args[1]
            if instance_id == self.created_id:
                self.created_id = None
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
            or not on the class name example: all BaseModel or all
        """
        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif arg in ["BaseModel"] or len(arg) == 0:
            print(self.created_model)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
            adding or updating attribute example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com".
            Usage: <class name> <id> <attribute name> <attribute value>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            input_id = args[1]
            if input_id != self.created_id and input_id[0].isdigit():
                print("** no instance found **")
            if not input_id[0].isdigit() and len(args) < 4:
                print("** attribute name missing **")
            else:
                att_name = args[2]
                att_value = args[3]
                if att_name not in ["id", "created_at", "updated_at"]:
                    setattr(self, att_name, att_value)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
    """def default(self, arg):
        dict_of_commands = {
                "EOF": self.do_EOF,
                "quit": self.do_quit
                }
        search = re."""
