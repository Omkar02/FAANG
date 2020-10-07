# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class disconnectedSubNet:
    def __init__(self, nodes, failedNode):
        self.graphs = {}
        self.visited = set()
        self.brokenSubNet = float('inf')
        self.runningNode = 0
        self.failedNode = failedNode
        self.generateGrapgs(nodes)
        print(self.graphs)

    def generateGrapgs(self, nodes):
        for start, destination in nodes:
            if start not in self.graphs:
                self.graphs[start] = []
            self.graphs[start].append(destination)

    def checkOutage(self):
        for node in self.failedNode:
            self.depthFirstSearch(node)
            print(f' -- > {self.runningNode}')
            self.brokenSubNet = min(self.brokenSubNet, self.runningNode)
            self.visited = set()
            self.runningNode = 0

        return self.brokenSubNet

    def depthFirstSearch(self, node):
        if node in self.visited:
            print(f'\t\t{node}')
            return

        self.visited.add(node)

        if node in self.graphs:
            for neighbour in self.graphs[node]:
                # print(neighbour, '================')
                self.depthFirstSearch(neighbour)

        self.runningNode += 1


nodes = [['A', 'B'], ['B', 'D'], ['D', 'G'], ['D', 'F'], ['F', 'H'], ['F', 'E'], ['B', 'C']]
fNode = ['B', 'F', 'H']


# d = disconnectedSubNet(nodes, fNode)
# print(d.checkOutage())


def checkDisconnection(nodes, fNode):
    graphs = {}
    print(nodes)
    for start, destination in nodes:

        if start not in graphs:
            graphs[start] = set()
        if destination not in graphs:
            graphs[destination] = set()

        graphs[start].add(destination)
        graphs[destination].add(start)

    minVal = float('inf')
    for failed in fNode:
        currMin = len(graphs[failed])
        print(f'{failed} - -> {len(graphs[failed])}')
        minVal = min(minVal, currMin)
    return minVal


print(checkDisconnection(nodes, fNode))
