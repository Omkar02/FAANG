import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def calcEquation(equations, values, queries):

    # make the graphs
    eqMap = {}
    for i in range(len(equations)):
        if equations[i][0]not in eqMap:
            eqMap[equations[i][0]] = []
        if equations[i][1] not in eqMap:
            eqMap[equations[i][1]] = []
        # print(equations[i][0])
        eqMap[equations[i][0]].append((equations[i][1], values[i]))
        eqMap[equations[i][1]].append((equations[i][0], 1 / values[i]))  # for complete the cycle

    print(f'The eqMap = {eqMap}')

    result = []

    for j in range(len(queries)):
        tempAns = -1
        runningAns = 1
        visited = []
        start = queries[j][0]
        end = queries[j][1]
        val = dfs(eqMap, start, end, tempAns, runningAns, visited)
        result.append(val)

    return result


def dfs(graph, start, end, tempAns, runningAns, visited):
    if start in visited or not start in graph:
        return -1.0
    if start == end:
        return runningAns

    visited.append(start)

    for j in graph[start]:
        ret = dfs(graph, j[0], end, tempAns, runningAns * j[1], visited)
        if ret != -1.0:
            return ret
    return -1.0


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]


print(calcEquation(equations, values, queries))
