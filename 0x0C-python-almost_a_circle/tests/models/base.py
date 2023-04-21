'''A base of all other classes in the model

Class:
    Base : a class to manage id
'''


class Base():
    '''A class to manage id

    Attributes:
        nb_objects : holds the number of objects, private
        '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes an instance of the class'''
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
