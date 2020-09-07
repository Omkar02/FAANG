# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


def minReorder(n, connections):
    edges = {(a, b) for a, b in connections}

    neighbours = {city: [] for city in range(n)}
    visit = set()
    changes = 0

    for a, b in connections:
        neighbours[a].append(b)
        neighbours[b].append(a)

    def dfs(city):
        nonlocal neighbours, visit, edges, changes

        for neighbour in neighbours[city]:
            if neighbour not in visit:
                if (neighbour, city) not in edges:
                    changes += 1

                visit.add(neighbour)
                dfs(neighbour)

    visit.add(0)
    dfs(0)

    return changes


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

print(minReorder(n, connections))
