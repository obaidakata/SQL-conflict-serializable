from DirectedGraph import DirectedGraph


class operation:
    operand = None
    transactionId = None
    variable = None

    def __init__(self, operand, transactionId, variable):
        self.operand = operand
        self.transactionId = transactionId
        self.variable = variable

    def __str__(self):
        return "{0},{1},{2}".format(self.operand, self.transactionId, self.variable)


class SQLConflictSerializable:
    graph = None
    userInput = None
    operations = []

    def __init__(self):
        self.getUserInput()
        self.initOperations()
        verticesList = self.getVerticesList()
        self.graph = DirectedGraph(verticesList)
        self.addEdgesToGraph()
        self.graph.topologicalSort()
        # self.graph.print()

    def initOperations(self):
        splittedInput = self.userInput.split(";")
        for command in splittedInput:
            indexOfP = command.find("(")
            operand = command[0]
            transactionsNumber = int(command[1:indexOfP])
            variable = command[indexOfP + 1:-1]
            operationToAdd = operation(operand, transactionsNumber, variable)
            self.operations.append(operationToAdd)

    def getVerticesList(self):
        listOfTransactions = []
        for operation in self.operations:
            if operation.transactionId not in listOfTransactions:
                listOfTransactions.append(operation.transactionId)
        return listOfTransactions

    def getUserInput(self):
        print("Please type your transactions list")
        self.userInput = input()

    def addEdgesToGraph(self):
        numberOfOperand = len(self.operations)
        for i in range(numberOfOperand):
            currentOperand = self.operations[i]
            for j in range(i + 1, numberOfOperand):
                if self.operations[j].variable == currentOperand.variable and self.operations[j].transactionId != currentOperand.transactionId:
                    if currentOperand.operand == 'R' and self.operations[j].operand == 'W':
                        self.graph.addEdge(currentOperand.transactionId, self.operations[j].transactionId)
                    elif currentOperand.operand == 'W' and self.operations[j].operand == 'R':
                        self.graph.addEdge(currentOperand.transactionId, self.operations[j].transactionId)
                    elif currentOperand.operand == 'W' and self.operations[j].operand == 'W':
                        self.graph.addEdge(currentOperand.transactionId, self.operations[j].transactionId)
