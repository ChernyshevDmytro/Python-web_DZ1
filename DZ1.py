from abc import abstractmethod, ABC
import json
import pickle


class Meta(type):
    number = 0
    def __new__(*args):                
        return type.__new__(*args)

    def __init__(self, *args):
        self.class_number=Meta.number
        Meta.number += 1 


    def __call__(cls, *args):
        instance = object.__new__(cls)

        return instance    
    

Meta.children_number = 0

class Cls1(metaclass=Meta):
    
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)

class SerializationInterface(metaclass=Meta):
    @abstractmethod
    def serialization(self):
        pass


class SerializationBin(SerializationInterface):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
    
    def serialization(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)


class SerializationJson(SerializationInterface):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
    
    def serialization(self):
        with open(self.filename, "wb") as file:
            json.dump(self, file)
