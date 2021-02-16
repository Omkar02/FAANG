# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class jNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.processing = False


class jobGraphs:
    def __init__(self, jobs):
        self.node = []
        self.graphs = {}
        for jb in jobs:
            self.graphs[jb] = jNode(jb)
            self.node.append(self.graphs[jb])

    def addReqs(self, job, prereqs):
        jobNode = self.graphs[job]
        jobPrereq = self.graphs[prereqs]

        jobNode.prereqs.append(jobPrereq)


def topologicalSort(jobs, dependency):
    graphs = createJobGraphs(jobs, dependency)
    return getOrderedJob(graphs)


def createJobGraphs(jobs, dependency):
    graphs = jobGraphs(jobs)
    for prereq, job in dependency:
        graphs.addReqs(job, prereq)
    return graphs


def getOrderedJob(graphs):
    orderedJob = []
    node = graphs.node
    while len(node):
        newNode = node.pop()
        containsCycle = dfs(newNode, orderedJob)
        if containsCycle:
            return False
    return True, list(reversed(orderedJob))


def dfs(node, orderedJob):
    if node.visited:
        return False
    if node.processing:
        return True

    node.processing = True
    for prereq in node.prereqs:
        containsCycle = dfs(prereq, orderedJob)
        if containsCycle:
            return False, orderedJob
    node.visited = True
    node.processing = False
    orderedJob.append(node.job)


numCourses = 2
node = [i for i in range(numCourses)]
dependency = prerequisites = [[1, 0]]

dependency = [[1, 0], [0, 1]]

print(topologicalSort(node, dependency))
