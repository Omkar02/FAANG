# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class flights:
    def __init__(self, edges):
        self.graph = {}
        self.constructGraph(edges)

    def constructGraph(self, edges):
        for scr, dst, wei in edges:
            if scr not in self.graph:
                self.graph[scr] = []
            self.graph[scr].append((wei, dst))

    def getCheapeastFlightWithK(self, scr, dst, k):
        heap = [(0, -k, scr)]
        while heap:
            heap.sort(key=lambda a: a[0])
            cost, idx, currNode = heap.pop(0)
            if dst == currNode:
                return cost

            for weight, edge in self.graph[currNode]:
                newCost = cost + weight
                if idx <= 0:
                    heap.append((newCost, idx + 1, edge))

        return -1


n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1

n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 0

f = flights(edges)
print(f.getCheapeastFlightWithK(src, dst, k))
