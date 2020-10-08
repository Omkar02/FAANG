# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Disjoint-Set', Difficult='Medium')

class DSU:
    def __init__(self, N):
        self.p = [0] * N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


def removeStones(stones):
    N = len(stones)
    dsu = DSU(20000)
    for x, y in stones:
        dsu.union(x, y + 10000)

    return N - len({dsu.find(x) for x, y in stones})


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]

print(removeStones(stones))
