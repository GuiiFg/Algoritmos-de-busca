
class GameSateControl:

    def __init__(self, state = None):

        """
        Modelo de estado para uso da classe:
        state = [[1,2,3],
                [4,5,6],
                [7,8,0]]

        Modelo para exportação e loading
        var = [1,2,3,4,5,6,7,8,0]
        """
        
        # 
        self.__state = self.__LoadState(state)
        self.__expandStates = None

        if state != None:
            self.__GenerateExpandStates()

    @property
    def state(self):
        return self.__ExportState()

    @state.setter
    def state(self, valueList):
        self.__state = self.__LoadState(valueList)

    # carrega um array para dentro do estado da classe
    def __LoadState(self, stateList : list):

        layer0 = []
        layer1 = []
        layer2 = []
        
        for value in stateList:
            if len(layer0) < 3:
                layer0.append(value)
            elif len(layer1) < 3:
                layer1.append(value)
            elif len(layer2) < 3:
                layer2.append(value)

        return [layer0, layer1, layer2]


    # exporta o estado do game para um array linear
    def __ExportState(self):
        stateList = []

        for layer in self.__state:
            for value in layer:
                stateList.append(value)

        return stateList

    def PrintState(self):

        print("--------- Print ---------")
        print("Estado atual:")

        for layer in self.__state:
            print("\t" + str(layer))

        print("-------------------------")

    def __GenerateExpandStates(self):
        
        zeroPosition = self.__FindZeroPosition()

    def __FindZeroPosition(self):

        position = [] # [layer(line), column]
        layerCount = 0
        for layer in self.__state:
            if 0 in layer:
                position.append(layerCount)
                positionCount = 0
                for value in layer:
                    if value == 0:
                        position.append(positionCount)
                        break
                    positionCount += 1

                break
            layerCount +=1

        return position



        

state = GameSateControl([2,8,7,1,0,3,4,5,6])

state.PrintState()