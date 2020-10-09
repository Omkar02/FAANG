# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class similar:
    def __init__(self, pairs):
        self.graph = {}
        self.visited = set()
        self.ans = True
        self.generateGraphs(pairs)
        self.cnt = [0]

    def generateGraphs(self, pairs):
        for scr, dst in pairs:
            if scr not in self.graph:
                self.graph[scr] = []
            if dst not in self.graph:
                self.graph[dst] = []

            self.graph[scr].append(dst)
            self.graph[dst].append(scr)

    def letsMatch(self, words1, words2):
        for scr, dst in zip(words1, words2):
            if scr != dst and not self.isSimilar(scr, dst):
                return False, self.cnt
            self.visited = set()
        return True, self.cnt

    def isSimilar(self, scr, dst):
        if scr in self.visited:
            return

        if scr == dst:
            return True
        else:
            self.visited.add(scr)
            if scr in self.graph:
                for nxtWord in self.graph[scr]:
                    self.cnt[0] += 1
                    if self.isSimilar(nxtWord, dst):
                        return True

            return False


words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]

s = similar(pairs)
print(s.letsMatch(words1, words2))
