#!/usr/bin/env python

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HNNBC gets cm.Cmd"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """help quit"""
        return True

    def do_EOF(self, line):
        """help end of file"""
        return True

    def emptyline(self):
        """Empty line method"""
        pass

    def do_create(self, model_type):
        """create methode"""
        model_types = [
            'BaseModel',
            'User',
            'City',
            'Amenity',
            'Place',
            'Review',
            'State'
        ]
        if model_type in model_types:
            if model_type == 'BaseModel':
                bm = BaseModel()
                bm.save()
                print(bm.id)
            if model_type == 'User':
                user = User()
                user.save()
                print(user.id)
            if model_type == 'City':
                city = City()
                city.save()
                print(city.id)
            if model_type == 'Amenity':
                amenity = Amenity()
                amenity.save()
                print(amenity.id)
            if model_type == 'Place':
                place = Place()
                place.save()
                print(place.city_id)
            if model_type == 'Review':
                review = Review()
                review.save()
                print(review.id)
            if model_type == 'State':
                state = State()
                state.save()
                print(state.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """show Method"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name and instance_id:
            all_objs = storage.all()
            key = class_name + "." + instance_id
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """destroy method"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name and instance_id:
            all_obj = storage.all()
            key = class_name + "." + instance_id
            if key in all_obj:
                del all_obj[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """do all method"""
        all_obj = storage.all()
        args = line.split()
        if len(args) == 0:
            for key in all_obj.keys():
                print(all_obj[key])
        elif args[0] in all_obj:
            for key in all_obj.keys():
                if type(all_obj[key]).__name__ == args[0]:
                    print(all_obj[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """update method"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        attr_value = args[3]
        if class_name and instance_id and attr_name and attr_value:
            all_objs = storage.all()
            key = class_name + "." + instance_id
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    """hbnb.do_create('BaseModel')
    hbnb.do_show('BaseModel instance_id')
    hbnb.do_destroy('BaseModel instance_id')
    hbnb.do_all('BaseModel')
    hbnb.do_update('BaseModel instance_id attr_name attr_value')
    """