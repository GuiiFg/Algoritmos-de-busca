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

        self.__frontierList["0"] = [de]

        self.__head = Node(de)

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
                    if self.__frontierList[layer][0] not in self.__closedList:
                        print(f"Trocando toExp para {self.__frontierList[layer][0]}")
                        toExpand.append(self.__frontierList[layer][0])
                        break
                    else:
                        print(f"deletei na layer {layer} : {self.__frontierList[layer][0]}")
                        self.__frontierList[layer].remove(
                            self.__frontierList[layer][0])

       
        if len(toExpand) > 0:
            toExpand = toExpand[0]
            print(self.__frontierList)
            print(toExpand)

            element = self.__FindelementByValue(toExpand)

            print(f"chei aqui com o elemento: {element.value}")

            if element.value == destino:
                self.__PrintResultFrom(element)
                print("Result Find!")
                breakpoint

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
                        element.childrens.append(
                            Node(x, layer=element.layer + 1, father=element))
                        if f"{element.layer + 1}" not in list(self.__frontierList.keys()):
                            print("Nova layer")
                            self.__frontierList[f"{element.layer + 1}"] = [x]
                            print(self.__frontierList[f"{element.layer + 1}"])
                        else:
                            print("Inserido")
                            self.__frontierList[f"{element.layer + 1}"].append(x)
                            print(self.__frontierList[f"{element.layer + 1}"])
                    else:
                        print(f"Já existe caminho para {x}")

            if element.value not in self.__closedList:
                self.__closedList.append(element.value)

            print(f"closeds: {self.__closedList}")

        else:
            print("Não existe para onde expandir")

        self.__IniciarBusca(destino)

        # print(f"elemento {element} valor: {element.value}, {canExpand}, {type(canExpand)}")

    def __WayExist(self, value) -> bool:

        layers = list(self.__frontierList.keys())
        layers.sort()

        for layer in layers:
            if len(self.__frontierList[layer]) > 0:
                if value in list(self.__frontierList[layer]):
                    return True

        return False

    def __FindelementByValue(self, value, root=None):

        print(f"procurando {value}")

        root = self.__head if root == None else root

        print(f"operando {root.value} == {value}")
        if root.value == value:
            print(f"achei {value}")
            return root
        else:
            print(f"procurando nos filhos de {root.value}")
            for x in root.childrens:
                print(f"Filho: {x.value}")
            print(f"filhos de {root.value} : {root.childrens}")
            for child in root.childrens:
                if self.__FindelementByValue(value, child) != None:
                    return self.__FindelementByValue(value, child)

    def __PrintResultFrom(self, element : Node):

        self.__result.append(element)

        if element.father != None:
            self.__PrintResultFrom(element.father)
            
