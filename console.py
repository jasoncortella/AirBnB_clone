#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from shlex import split
import re


class HBNBCommand(cmd.Cmd):
    """ console """

    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """ do nothing for an empty line """
        pass

    def do_create(self, arg):
        """
        Example usage - "create BaseModel"
        create a new class instance, saves it to JSON,  and print its id
        """
        if not arg:
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
        show command to print the str representation of an instance
        """
        arglist = split(arg)
        if len(arglist) > 1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arg:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif iid not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[iid])

    def do_destroy(self, arg):
        """
        Example usage - "destroy BaseModel 121212"
        destroy command to delete an instance based on class name and id
        """
        arglist = split(arg)
        if len(arglist) > 1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arg:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif iid not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[iid]
            storage.save()

    def do_all(self, arg):
        """
        Example usage 1 - "all"
        Example usage 2 - "all BaseModel"
        all command to print all string representations of instances
            - Can decide whether or not to choose a single class
        """
        arglist = split(arg)
        if len(arglist) and arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            plist = []
            for obj in storage.all().values():
                if len(arglist) == 0:
                    plist.append(obj.__str__())
                elif arglist[0] == obj.__class__.__name__:
                    plist.append(obj.__str__())
            print(plist)

    def do_update(self, arg):
        """
        Example usage - update BaseModel 1234 email "aibnb@holbertonschool.com"
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        update command to update an instance based on the class name
        and id by adding or updating attribute
        """
        arglist = split(arg)
        if len(arglist) > 1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arg:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif iid not in storage.all():
            print("** no instance found **")
        elif len(arglist) == 2:
            print("** attribute name missing **")
        elif len(arglist) == 3:
            print("** value missing **")
        else:
            setattr(storage.all()[iid], arglist[2], arglist[3])
            storage.all()[iid].save()

    def default(self, arg):
        """ default methods """
        for k in self.__classes:
            if arg == (k + '.all()'):
                self.do_all(k)
            elif arg == (k + '.count()'):
                count = 0
                for key in storage.all():
                    if k in key:
                        count += 1
                print(count)
            elif arg.startswith(k + ".show(") and arg.endswith(")"):
                x = re.search('"(.+?)"', arg)
                if x:
                    iid = x.group(1)
                self.do_show(k + " " + iid)
            elif arg.startswith(k + ".destroy(") and arg.endswith(")"):
                x = re.search('"(.+?)"', arg)
                if x:
                    iid = x.group(1)
                self.do_destroy(k + " " + iid)
            elif arg.startswith(k + ".update(") and arg.endswith(")"):
                start = arg.find('(')
                end = arg.find(')')
                x = arg[start:end]
                x = x.replace(',', '')
                al = split(x[1:])
                self.do_update('{} {} {} "{}"'.format(k, al[0], al[1], al[2]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
