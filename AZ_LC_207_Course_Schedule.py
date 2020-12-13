# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class jobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.processing = False


class jobGraphs:
    def __init__(self, jobs):
        self.nodes = []
        self.graphs = {}
        for jb in jobs:
            self.graphs[jb] = jobNode(jb)
            self.nodes.append(self.graphs[jb])

    def addReqs(self, job, prereqs):
        jobNode = self.graphs[job]
        jobPrereq = self.graphs[prereqs]

        jobNode.prereqs.append(jobPrereq)


def topologicalSort(jobs, dependency):
    graphs = createJobGraphs(jobs, dependency)
    return getOrderedJob(graphs)


def createJobGraphs(jobs, dependency):
    graphs = jobGraphs(jobs)
    for prepq, job in dependency:
        graphs.addReqs(job, prepq)
    return graphs


def getOrderedJob(graphs):
    orderedJob = []
    node = graphs.nodes
    while len(node):
        newNode = node.pop()
        containsCycle = DFS(newNode, orderedJob)
        if containsCycle:
            return False
    return True, list(reversed(orderedJob))


def DFS(node, orderedJob):
    if node.visited:
        return False
    if node.processing:
        return True

    node.processing = True
    for prereq in node.prereqs:
        containsCycle = DFS(prereq, orderedJob)
        if containsCycle:
            return False, orderedJob

    node.visited = True
    node.processing = False
    orderedJob.append(node.job)


node = [0, 1, 2, 3]
dependency = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(f'the Order = {topologicalSort(node, dependency)}')
