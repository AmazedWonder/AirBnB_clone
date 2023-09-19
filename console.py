#!/usr/bin/python3
"""Module for the command interpreter"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""

    prompt = "(hbnb) "

    def default(self, arg):
        """Catch command"""
        self._precmd(arg)

    def _precmd(self, arg):
        """ test for class.synatx"""
        matc = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not matc:
            return arg
        class_name = matc.group(1)
        function = matc.group(2)
        args = matc.group(3)
        matc_id_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if matc_id_args:
            uid = matc_id_args.group(1)
            attr_or_dict = matc_id_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_value = ""
        if function == "update" and attr_or_dict:
            m_dict = re.search('^({.*})$', attr_or_dict)
            if m_dict:
                self.update_dict(class_name, uid, m_dict.group(1))
                return ""
            attr_value = re.serch(
                    '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if attr_value:
                attr_and_value = (attr_value.group(1) or "") + " "
                + (attr_value.group(2) or "")
        cmnd = function + " " + class_name + " " + uid + " " + attr_and_value
        self.onecmd(cmnd)
        return cmnd

    def do_EOF(self, line):
        """End file"""
        return True

    def do_quit(self, line):
        """quit the console"""
        return True

    def help_quit(self):
        """exit the program"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """exit with control D"""
        print("Exit the program (Ctrl+D)")

    def emptyline(self):
        """Empty line on console"""
        pass

    def do_create(self, arg):
        """creating a class or instances"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist**")
        else:
            instnce = storage.classes()[arg]()
            instnce.save()
            print(instnce.id)

    def do_count(self, arg):
        """Count instances of class"""
        arguments = arg.split(' ')
        if not arg[0]:
            print("** class name missing **")
        elif arguments[0] not in storage.classes():
            print("** class does't exist **")
        else:
            matc = [
                i for i in storage.all() if i.startwith(
                    arg[0] + '.')]
            print(len(matc)

    def do_show(self, arg):
        """show all the classes and instances"""
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
        """destroying classes and instances when created"""
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
        """show all the classes in json file"""
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
        """Updating the files in json"""
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
