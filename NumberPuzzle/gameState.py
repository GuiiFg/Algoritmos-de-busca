
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
        self.__expandStates = []

        if state != None:
            self.__CalculateExpandStates()

    @property
    def state(self):
        return self.__ExportState()

    @state.setter
    def state(self, valueList):
        self.__state = self.__LoadState(valueList)
        self.__CalculateExpandStates()

    @property
    def expandStates(self):
        return self.__expandStates

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
    def __ExportState(self, state = None):
        state = self.__state if state == None else state
        stateList = []

        for layer in state:
            for value in layer:
                stateList.append(value)

        return stateList

    def PrintState(self, state = None):

        state = self.__state if state == None else state

        print("--------- Print ---------")
        print("Estado atual:")

        for layer in self.__state:
            print("\t" + str(layer))

        print("-------------------------")

    def __CalculateExpandStates(self):
        
        zeroPosition = self.__FindZeroPosition() # [layer, column]

        canChange = []

        if zeroPosition[0] == 0:
            canChange.append([1,zeroPosition[1]])

            if zeroPosition[1] == 1:
                canChange.append([zeroPosition[0],0])
                canChange.append([zeroPosition[0],2])
            else:
                canChange.append([zeroPosition[0],1])

        elif zeroPosition[0] == 1:

            canChange.append([0,zeroPosition[1]])
            canChange.append([2,zeroPosition[1]])

            if zeroPosition[1] == 1:
                canChange.append([zeroPosition[0],0])
                canChange.append([zeroPosition[0],2])
            else:
                canChange.append([zeroPosition[0],1])

        elif zeroPosition[0] == 2:
            canChange.append([1,zeroPosition[1]])

            if zeroPosition[1] == 1:
                canChange.append([zeroPosition[0],0])
                canChange.append([zeroPosition[0],2])
            else:
                canChange.append([zeroPosition[0],1])

        self.__GenerateExpandStates(canChange, zeroPosition)

    def __GenerateExpandStates(self, canChange : list, zeroPosition: list):

        newStates = []
        
        for position in canChange:
            newState = []

            for layer in self.__state:
                values = []
                for value in layer:
                    values.append(int(value))
                newState.append(values)
                
            
            newState[zeroPosition[0]][zeroPosition[1]] = newState[position[0]][position[1]]
            newState[position[0]][position[1]] = 0
            
            newStates.append(newState)

        self.__expandStates = []
        
        for state in newStates:
            self.__expandStates.append(self.__ExportState(state))

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
