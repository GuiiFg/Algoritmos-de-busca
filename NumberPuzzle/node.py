
from NumberPuzzle.gameState import GameSateControl


class Node:

    def __init__(self, gameState: GameSateControl, father=None, layer = 0):

        self.__gameState = gameState
        self.__father = father
        self.__layer = layer
        self.__childrens = []

    @property
    def gameState(self):
        return self.__gameState

    @gameState.setter
    def gameState(self, value):
        self.__gameState = value

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
