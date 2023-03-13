import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name >.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
