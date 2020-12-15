# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = {}
        self.temp = []

    def DFSUtil(self, v, visited):
        print(self.adj)
        visited[v] = True
        self.temp.append(v)
        for i in self.adj[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        if w not in self.adj:
            self.adj[w] = []

        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                self.DFSUtil(v, visited)
                cc.append(self.temp)
                self.temp = []
        return cc



# Create a graph given in the above diagram
# 5 vertices numbered from 0 to 4
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
cc = g.connectedComponents()
print("Following are connected components")
print(cc)
