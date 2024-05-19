import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_obj = eval("{}()".format(class_name))
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        objs = FileStorage().all()
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        objs = FileStorage().all()
        if obj_key in objs:
            del objs[obj_key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        objs = FileStorage().all()
        if not arg:
            print([str(obj) for obj in objs.values()])
            return
        args = arg.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objs.items() if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        objs = FileStorage().all()
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        setattr(objs[obj_key], attr_name, attr_value)
        FileStorage().save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

