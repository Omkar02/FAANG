# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class division:
    def __init__(self, equations, values):
        self.graph = {}
        self.visited = set()
        self.ans = []
        self.generateGraph(equations, values)

    def generateGraph(self, equations, values):
        for idx, node in enumerate(equations):
            if node[0] not in self.graph:
                self.graph[node[0]] = []

            if node[1] not in self.graph:
                self.graph[node[1]] = []

            self.graph[node[0]].append((node[1], values[idx]))
            self.graph[node[1]].append((node[0], 1 / values[idx]))

    def depthFirstSearch(self, start, end, runningAns):
        if start in self.visited or start not in self.graph:
            return -1.0
        if start == end:
            return runningAns

        self.visited.add(start)

        for neiNode, val in self.graph[start]:
            ret = self.depthFirstSearch(neiNode, end, runningAns * val)
            if ret != -1.0:
                return ret
        return -1.0

    def evaluate(self, queries):
        for e1, e2 in queries:
            self.ans.append(self.depthFirstSearch(e1, e2, 1))
            self.visited = set()

        return self.ans


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

d = division(equations, values)
print(d.graph)
d.evaluate(queries)
print(d.ans)
# [6.0, 0.5, -1.0, 1, -1.0]
