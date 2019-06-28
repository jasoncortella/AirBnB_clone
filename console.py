#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ console """
    prompt = '(hbnb) '

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def do_create(self, *args):
        """create command to exit the program"""
        return True #PLACEHOLDER

    def do_show(self, *args):
        """show command to exit the program"""
        return True #PLACEHOLDER

    def do_destroy(self, *args):
        """destroy command to exit the program"""
        return True #PLACEHOLDER

    def do_all(self, *args):
        """all command to exit the program"""
        return True #PLACEHOLDER

    def do_update(self, *args):
        """update command to exit the program"""
        return True #PLACEHOLDER


if __name__ == '__main__':
    HBNBCommand().cmdloop()
