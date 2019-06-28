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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
