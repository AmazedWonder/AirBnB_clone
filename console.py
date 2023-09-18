#!/usr/bin/python3

import cmd
import re
from models import storage
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        End file
        """
        return True

    def do_quit(self, line):
        """
        quit the console
        """
        return True

    def help_quit(self):
        """
        exit the program
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        exit with control D
        """
        print("Exit the program (Ctrl+D)")

    def emptyline(self):
        """
        Empty line on console
        """
        pass

    def do_create(self, arg):
        """
        creating a class or instances
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist**")
        else:
            instnce = storage.classes()[arg]()
            instnce.save()
            print(instnce.id)

    def do_show(self, arg):
        """
        show all the classes and instances
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            arguments = arg.split(' ')
            if arguments[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                k = f"{arguments[0]}.{arguments[1]}"
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_destroy(self, arg):
        """
        destroying classes and instances when created
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            arguments = arg.split(' ')
            if arguments[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                k = f"{arguments[0]}, {arguments[1]}"
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[k]
                    storage.save()

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_all(self, arg):
        """
        show all the classes in json file
        """
        if arg:
            arguments = arg.split(' ')
            if not arguments or arguments[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == arguments[0]]
                print(obj_list)
        else:
            obj_new_list = [str(obj) for key, obj in storage.all().items()]
            print(obj_new_list)

    def do_update(self, arg):
        """
        Updating the files in json
        """
        if arg is None or arg == "":
            print("** class name missing **")
            return

        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match_regx = re.search(regx, arg)
        class_name = match_regx.group(1)
        uid = match_regx.group(2)
        attr = match_regx.group(3)
        attr_value = match_regx.group(4)
        if not match_regx:
            print(" ** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attr:
                print("** attribute name missing **")
            elif not attr_value:
                print("** value missing **")
            else:
                casting = None
                if not re.search('^".*"$', attr_value):
                    if '.' in attr_value:
                        casting = float
                    else:
                        casting = int
                else:
                    attr_value = attr_value.replace('"', '')
                attributes = storage.attributes()[class_name]
                if attr in attributes:
                    attr_value = attributes[attr](attr_value)
                elif casting:
                    try:
                        attr_value = casting(attr_value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attr, attr_value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
