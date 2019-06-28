#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """ console """

    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel,
                 "User": BaseModel,
                 "State": BaseModel,
                 "City": BaseModel,
                 "Amenity": BaseModel,  # Placeholders, replace once classes
                 "Place": BaseModel,    # are all created
                 "Review": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """
        Example usage - "create BaseModel"
        create a new class instance, saves it to JSON,  and print its id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.__classes[arg]()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        """
        Example usage - "show BaseModel 121212"
        show command to exit the program
        """
        arglist = split(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arglist[0], arglist[1]) not in storage.all()):
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(arglist[0], arglist[1])])

    def do_destroy(self, arg):
        """destroy command to exit the program"""
        return True  # PLACEHOLDER

    def do_all(self, *args):
        """all command to exit the program"""
        return True  # PLACEHOLDER

    def do_update(self, *args):
        """update command to exit the program"""
        return True  # PLACEHOLDER


if __name__ == '__main__':
    HBNBCommand().cmdloop()
