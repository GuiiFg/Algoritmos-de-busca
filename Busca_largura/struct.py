from cgi import print_form
from logging import root
from subprocess import TimeoutExpired
from Busca_largura.node import Node


class SearchTree:
    def __init__(self, map: dict):

        self.__map = map
        self.__start = None
        self.__end = None
        self.__closedList: list = []
        self.__frontierList: dict = {}
        self.__result: list = []
        self.__head = None

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, value):
        self.__map = value

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        self.__start = value

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        self.__end = value

    @property
    def closedList(self):
        return self.__closedList

    @property
    def frontierList(self):
        return self.__frontierList

    @property
    def result(self):
        return self.__result

    def Buscar(self, de, para):

        self.__ValidarExistencia([de, para])

        self.__head = Node(de)

        self.__frontierList["0"] = [self.__head]

        self.__IniciarBusca(para)

    def __ValidarExistencia(self, toValidate: list):

        for x in toValidate:
            if x not in self.__map.keys():
                raise ValueError(f"O ponto {str(x)} não existe no mapa!")

    def __IniciarBusca(self, destino):

        print("---------------------------------")

        layers = list(self.__frontierList.keys())
        layers.sort()

        toExpand = []

        for layer in layers:
            print(f"layer: {layer}")
            if len(self.__frontierList[layer]) > 0:
                for x in range(len(self.__frontierList[layer])):
                    print(f"entrei na layer {layer}")
                    if self.__frontierList[layer][0].value not in self.__closedList:
                        print(f"Trocando toExp para {self.__frontierList[layer][0].value}")
                        toExpand.append(self.__frontierList[layer][0])
                    else:
                        print(f"deletei na layer {layer} : {self.__frontierList[layer][0].value}")
                        self.__frontierList[layer].remove(
                            self.__frontierList[layer][0])

        withoutFrontier = True
        for layer in layers:
            if len(self.__frontierList[layer]) > 0:
                withoutFrontier = False

        finded = False

        if len(toExpand) > 0:
            toExpand = toExpand[0]
            print(self.__frontierList)
            print(toExpand.value)

            element = toExpand
            
            print(f"achei! elemento: {element.value}")

            if element.value == destino:
                self.__PrintResultFrom(element)
                print("Result Find!")
                return self.__showResult()
                finded = True

            canExpand: list = self.__map[f"{element.value}"]

            for x in self.__closedList:
                if x in canExpand:
                    canExpand.remove(x)

            canExpand.sort()

            print(f"canExp: {canExpand}")

            if len(canExpand) > 0:
                for x in canExpand:
                    if not self.__WayExist(x):
                        print(f"Registrando {x} como filho de {element.value}")
                        son = Node(x, layer=element.layer + 1, father=element)
                        element.childrens.append(son)
                        if f"{element.layer + 1}" not in list(self.__frontierList.keys()):
                            print("Nova layer")
                            self.__frontierList[f"{element.layer + 1}"] = [son]
                            print(self.__frontierList[f"{element.layer + 1}"])
                        else:
                            print("Inserido")
                            self.__frontierList[f"{element.layer + 1}"].append(son)
                            print(self.__frontierList[f"{element.layer + 1}"])
                    else:
                        print(f"Já existe caminho para {x}")

            if element.value not in self.__closedList:
                self.__closedList.append(element.value)

            print(f"closeds: {self.__closedList}")

        else:
            print("Não existe para onde expandir")

        if not finded and not withoutFrontier:
            self.__IniciarBusca(destino)
        elif withoutFrontier and not finded:
            print('\033[1;31m' + "Não existe caminho!" + '\033[0;37m')


        # print(f"elemento {element} valor: {element.value}, {canExpand}, {type(canExpand)}")

    def __WayExist(self, value) -> bool:

        layers = list(self.__frontierList.keys())
        layers.sort()

        for layer in layers:
            if len(self.__frontierList[layer]) > 0:
                withWay = []
                for x in list(self.__frontierList[layer]):
                    withWay.append(x.value)
                if value in withWay:
                    return True

        return False

    def __PrintResultFrom(self, element : Node):

        self.__result.append(element)

        print(f"Caminho correto para: {element.value}")

        if element.father != None:
            self.__PrintResultFrom(element.father)
            
    def __showResult(self):

        self.__result = self.result[::-1]

        caminho = ""

        for x in self.__result:
            caminho += f" -> {x.value}"

        print('\033[1;32m' + caminho + '\033[0;37m')

        caminho = []
        for x in self.__result:
            caminho.append(x.value)

        print(caminho)

        return caminho
            
