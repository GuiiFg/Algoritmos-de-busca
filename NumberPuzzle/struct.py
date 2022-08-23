from NumberPuzzle.node import Node
from NumberPuzzle.gameState import GameSateControl
import time

class SearchTree:
    def __init__(self):

        self.__closedList: list = []
        self.__frontierList: dict = {}
        self.__result: list = []
        self.__head = None

    def __ReiniciarVars(self):
        self.__closedList: list = []
        self.__frontierList: dict = {}
        self.__result: list = []
        self.__head = None

    def BuscarResultado(self, estadoInicial : list, estadoFinal : list):
        
        self.__ReiniciarVars()

        gameInitialState = GameSateControl(estadoInicial)
        self.__head = Node(gameInitialState)
        self.__frontierList["0"] = [self.__head]

        self.__BuscarPor(estadoFinal)

    def __BuscarPor(self, destino : list):

        print("Aguardando 0.5s")

        #time.sleep(0.5)
        
        #print("---------------------------------")

        layers = list(self.__frontierList.keys())
        layers.sort()

        toExpand = []

        for layer in layers:
            #print(f"layer: {layer}")
            if len(self.__frontierList[layer]) > 0:
                for node in self.__frontierList[layer]:
                    #print(f"entrei na layer {layer}")
                    if node.gameState.state not in self.__closedList:
                        #print(f"Trocando toExp para {node.gameState.state}")
                        toExpand.append(node)
                    else:
                        #print(f"deletei na layer {layer} : {node.gameState.state}")
                        self.__frontierList[layer].remove(
                            node)

        withoutFrontier = True
        for layer in layers:
            if len(self.__frontierList[layer]) > 0:
                withoutFrontier = False

        finded = False

        if len(toExpand) > 0:
            toExpand : Node = self.__SelectNodeToExpand(toExpand, destino)
            #print(self.__frontierList)
            toExpand.gameState.PrintState()

            element = toExpand

            #print(f"achei! elemento: {element.gameState.state}")

            if element.gameState.state == destino:
                self.__PrintResultFrom(element)
                print("Result Find!")
                return self.__showResult()
                finded = True

            canExpand: list = element.gameState.expandStates

            for x in self.__closedList:
                if x in canExpand:
                    canExpand.remove(x)

            canExpand.sort()

            #print(f"canExp: {canExpand}")

            if len(canExpand) > 0:
                for x in canExpand:
                    if not self.__WayExist(x):
                        #print(f"Registrando {x} como filho de {element.gameState.state}")
                        son = Node(gameState=GameSateControl(x), layer=element.layer + 1, father=element)
                        element.childrens.append(son)
                        if f"{element.layer + 1}" not in list(self.__frontierList.keys()):
                            #print("Nova layer")
                            self.__frontierList[f"{element.layer + 1}"] = [son]
                            
                        else:
                            #print("Inserido")
                            self.__frontierList[f"{element.layer + 1}"].append(
                                son)

                        #print(self.__frontierList[f"{element.layer + 1}"])
                    else:
                        print(f"Já existe caminho para {x}")

            if element.gameState.state not in self.__closedList:
                self.__closedList.append(element.gameState.state)

            #print(f"closeds: {self.__closedList}")

        else:
            print("Não existe para onde expandir")

        if not finded and not withoutFrontier:
            self.__BuscarPor(destino)
        elif withoutFrontier and not finded:
            print('\033[1;31m' + "Não existe caminho!" + '\033[0;37m')

    def __WayExist(self, value) -> bool:

        layers = list(self.__frontierList.keys())
        layers.sort()

        for layer in layers:
            if len(self.__frontierList[layer]) > 0:
                withWay = []
                for x in list(self.__frontierList[layer]):
                    withWay.append(x.gameState.state)
                if value in withWay:
                    return True

        return False

    def __PrintResultFrom(self, node : Node):

        print("------------------ Resultado")
        node.gameState.PrintState()
        print("----------------------------")
        raise ValueError("N eh erro")

    def __SelectNodeToExpand(self, nodeList : list[Node], destino:list):

        bestResult = [0, None]

        for node in nodeList:
            similares = [True for x in range(len(node.gameState.state)) if node.gameState.state[x] == destino[x]]

            score = similares.count(True)

            print(f"Node {node} similarHate: {score}")

            if score > bestResult[0]:
                bestResult = [score, node]
            elif score == bestResult[0]:

                bestNode = bestResult[1] if bestResult[1].layer <= node.layer else node
                bestResult = [score, bestNode]

        return bestResult[1]

        
