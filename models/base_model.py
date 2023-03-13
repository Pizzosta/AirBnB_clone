#!/usr/bin/pyhon3
"""
Defines the BaseModel class.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods of the AirBnB project
    """
    def __init__(self, *args, **kwargs):
        """initializes all attributes of a new BaseModel
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], time_format)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """returns class name, id and attribute dictionary -
        the print/str representation of the BaseModel instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()
        storage.new(self)

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datetimes converted to strings
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
