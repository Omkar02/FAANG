class gNode():
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjList = []
        self.perReq = []
        self.ancenstor = None
        self.processing = False

    def addNodes(self, arr):
        self.adjList.extend(arr)


class Graphs():
    def __init__(self):
        self.head = None
        self.graphsNode = {}

    def insert(self, data):
        return gNode(data)

    def setHead(self, data):
        self.head = gNode(data)

    def getHead(self):
        return self.head

    def printGraphs(self):
        node = self.head
        qu = [node]
        while qu:
            node = qu.pop()
            print(node.data if not node.data else '')
            for val in node.adjList:
                print(f'{node.data}---->{val.data}', end=' ')
                qu.append(val)


g = Graphs()

# g.setHead('k')

# a = g.insert('a')
# b = g.insert('b')
# c = g.insert('c')
# d = g.insert('d')
# e = g.insert('e')
# f = g.insert('f')


# g.getHead().addNodes([a, b, c])
# a.addNodes([d, e])
# b.addNodes([f])

# g.printGraphs()
