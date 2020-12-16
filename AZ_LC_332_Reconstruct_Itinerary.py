# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


class itenery:
    def __init__(self, plan):
        self.graph = {}
        self.visited = set()
        self.iter = []
        self.creatGraph(plan)

    def creatGraph(self, plan):

        all_places = set()
        for place in plan:
            curr, dest = place[0], place[1]
            if curr not in self.graph:
                self.graph[curr] = []

            self.graph[curr].append(dest)

    def getItenery(self, node):
        self.iter.append(node)
        if node in self.visited:
            return
        self.visited.add(node)

        if node in self.graph:
            for v in self.graph[node]:
                self.getItenery(v)


plan = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# plan = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]


i = itenery(plan)
i.getItenery('JFK')

print(i.iter)

print(["JFK", "MUC", "LHR", "SFO", "SJC"])
# print(sorted(["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]))
