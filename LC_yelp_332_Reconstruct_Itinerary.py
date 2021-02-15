# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class itenary:
    def __init__(self, tickets):
        self.completeItenary = []
        self.visited = set()
        self.connection = self.getConnections(tickets)
        self.generateItenary('JFK')

    def getConnections(self, tickets):
        connection = {}
        for scr, dst in tickets:
            if scr not in connection:
                connection[scr] = []
            connection[scr].append(dst)
            connection[scr].sort()

        return connection

    def generateItenary(self, currLoc):
        self.completeItenary.append(currLoc)
        if currLoc in self.visited:
            return
        self.visited.add(currLoc)
        if currLoc in self.connection:
            for loc in self.connection[currLoc]:
                self.generateItenary(loc)

    def getCompleteItenary(self):
        return self.completeItenary


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

i = itenary(tickets)
print(i.getCompleteItenary())
