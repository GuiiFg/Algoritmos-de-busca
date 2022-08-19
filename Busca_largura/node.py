class Node:
    def __init__(self, value, layer: int = 0, father=None):

        self.__layer = layer
        self.__father = father
        self.__childrens = []
        self.__value = value

    @property
    def layer(self):
        return self.__layer

    @layer.setter
    def layer(self, value):
        self.__layer = value

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        self.__father = value

    @property
    def childrens(self):
        return self.__childrens

    @childrens.setter
    def childrens(self, value):
        self.__childrens = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
