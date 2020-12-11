# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree
readyTree.printTree()

ans = []


class Solution:
    def __init__(self):
        self.res = []
        self.parent = {}
        self.visited = set()

    def distanceK(self, root, target, K):
        self.getParents(root, None)
        return self.bfs(target, K)

    def getParents(self, node, parent):
        if not node:
            return

        self.parent[node.data] = parent

        self.getParents(node.lChild, node)
        self.getParents(node.rChild, node)

    def bfs(self, start, K):
        q = [(start, 0)]
        while q:
            node, dist = q.pop(0)
            if node not in self.visited:
                if dist == K:
                    self.res.append(node.data)
                self.visited.add(node)
                if node.lChild:
                    q.append((node.lChild, dist + 1))
                if node.rChild:
                    q.append((node.rChild, dist + 1))

                if self.parent[node.data]:
                    q.append((self.parent[node.data], dist + 1))


s = Solution()
s.distanceK(readyTree.getHead(), readyTree.getHead(), 1)
print(s.res)
