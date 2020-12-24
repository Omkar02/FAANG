# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class fCircle:
    def __init__(self, connection):
        self.connection = connection
        self.visited = set()
        self.number_of_circle = 0
        self.rowLen = len(connection)

    def find_friend_circle(self):
        for friend in range(self.rowLen):
            if friend not in self.visited:
                self.depth_first_scan(friend)
                self.number_of_circle += 1
        return self.number_of_circle

    def depth_first_scan(self, friend):
        self.visited.add(friend)
        for ifreind, value in enumerate(self.connection[friend]):
            if value and ifreind not in self.visited:
                self.depth_first_scan(ifreind)


connection = [[1, 1, 0],
              [1, 1, 0],
              [0, 0, 1]]
c = fCircle(connection)
c.find_friend_circle()
print(c.number_of_circle)
