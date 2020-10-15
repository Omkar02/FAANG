# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


class SnapshotArray:
    def __init__(self, length):
        self.snapId = 0
        self.store = {}
        self.array = [None for _ in range(length)]
        self.length = length

    def sets(self, index, val):
        if index > self.length:
            return -1

        self.array[index] = val

    def snap(self):
        self.store[self.snapId] = self.array
        self.array = [None for _ in range(self.length)]
        temp = self.snapId
        self.snapId += 1
        return temp

    def get(self, index, snapId):
        if snapId not in self.store or index > self.length:
            return -1

        return self.store[snapId][index]


["SnapshotArray", "set", "snap", "set", "get"]
[[3], [0, 5], [], [0, 6], [0, 0]]


s = SnapshotArray(3)
print(s.sets(0, 5))
print(s.snap())
print(s.sets(0, 6))
print(s.get(0, 0))
# Output: [null,null,0,null,5]
