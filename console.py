#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command processor for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if key.startswith(args[0]):
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('\"')
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

