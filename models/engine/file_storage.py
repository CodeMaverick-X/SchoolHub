#!/usr/bin/python3
"""__file_storage__
    Desc: module that conatins class FileStorage
    that handles the serialization of data in json
"""

import json
import models
from models.base_model import BaseModel
from models.user import User

classes = {"User": User, "BaseModel": BaseModel}

class FileStorage():
    """__FileStorage__
        Desc: serialize objects to json and vise versa.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Desc: returns a dictionary of objects
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def get_user(self, username=None):
        """get the user object for a username if exist"""
        users = models.storage.all(User)
        
        if username:
            for user in users.values():
                if (user.username == username):
                    return user
        return None

    def unique(self, username=None):
        """check if a username already exist in the system"""
        users = models.storage.all(User)

        if username:
            for user in users.values():
                if (user.username == username):
                    return False
            return True
        else:
            return False

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

