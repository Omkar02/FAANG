# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Hard')


class divide:
    def __init__(self, equations, values):
        self.eqGraphs = {}
        self.visited = set()
        self.result = []
        self._createGraphs(equations, values)

    def _createGraphs(self, equations, values):
        for idx, node in enumerate(equations):
            if node[0] not in self.eqGraphs:
                self.eqGraphs[node[0]] = []

            if node[1] not in self.eqGraphs:
                self.eqGraphs[node[1]] = []

            self.eqGraphs[node[0]].append([node[1], values[idx]])
            self.eqGraphs[node[1]].append([node[0], 1 / values[idx]])

    def evaluate(self, queries):
        for eq in queries:
            self.result.append(self.depthFirstSearch(eq[0], eq[1], 1))
            self.visited = set()

    def depthFirstSearch(self, start, end, runningAns):
        if start in self.visited or start not in self.eqGraphs:
            return -1.0
        if start == end:
            return runningAns

        self.visited.add(start)

        for node in self.eqGraphs[start]:
            ret = self.depthFirstSearch(node[0], end, runningAns * node[1])
            if ret != -1.0:
                return ret
        return -1.0


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

d = divide(equations, values)
print(d.eqGraphs)
d.evaluate(queries)
print(d.result)
