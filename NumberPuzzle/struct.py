from NumberPuzzle.node import Node

class SearchTree:
    def __init__(self):

        self.__closedList: list = []
        self.__frontierList: dict = {}
        self.__result: list = []
        self.__head = None

    def BuscarResultado(estadoInicial, estadoFinal):
        pass