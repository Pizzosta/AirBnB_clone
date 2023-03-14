import json


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
        serialized_objects = {}

        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**value)

        except FileNotFoundError:
            return
