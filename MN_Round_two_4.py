# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

# -------------------------------------------------------------#


class BoggleBoard:
    def __init__(self, board, dictoinary):
        self.tries = Tries()
        for w in dictoinary:
            self.tries.addword(w)
        self.board = board
        self.rowLen = len(board)
        self.colLen = len(board[0])
        self.visited = [[False for _ in range(self.colLen)] for _ in range(self.rowLen)]
        self.ans = {}
        self.findWord()

    def findWord(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                self.checkWordExits((r, c), self.tries.root)

    def checkWordExits(self, cord, tries):
        if self.visited[cord[0]][cord[1]]:

            return
        currWord = self.board[cord[0]][cord[1]]
        if currWord not in tries:
            return
        self.visited[cord[0]][cord[1]] = True
        nxtTries = tries[currWord]
        if '*' in nxtTries:
            self.ans[nxtTries['*']] = True
        neighbours = self.getNeighbour(cord)
        for ne in neighbours:
            self.checkWordExits(ne, nxtTries)

        self.visited[cord[0]][cord[1]] = False

    def getNeighbour(self, cord):
        neig = []
        rowRange = range(0, self.rowLen)
        colRange = range(0, self.colLen)
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for d in direction:
            newR, newC = cord[0] + d[0], cord[1] + d[1]
            if newR in rowRange and newC in colRange:
                neig.append((newR, newC))
        return neig


class Tries:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def addword(self, words):
        current = self.root
        for letter in words:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = words

    def printTries(self):
        return self.root


board = [['t', 'h', 'i', 's', 'i', 's', 'a'],
         ['s', 'i', 'm', 'p', 'l', 'e', 'x'],
         ['b', 'x', 'x', 'x', 'x', 'e', 'b'],
         ['x', 'o', 'g', 'g', 'l', 'x', 'o'],
         ['x', 'x', 'x', 'd', 't', 'r', 'a'],
         ['r', 'e', 'p', 'e', 'a', 'd', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
         ['n', 'o', 't', 'r', 'e', '-', 'p'],
         ['x', 'x', 'd', 'e', 't', 'a', 'e']]

words = ['this', 'is', 'not', 'a', 'simple',
         'boggle', 'board', 'test', 'repated', 'notre-peated']

# b = BoggleBoard(board, words)
# [print(x) for x, _ in b.ans.items()]


# -------------------------------------------------------------#

def getPermutation(arr):
    permutation = []
    _permHelper(arr, permutation, 0)
    return permutation


def _permHelper(arr, permutation, idx):
    if idx == len(arr) - 1:
        permutation.append(arr[:])
    else:
        for j in range(idx, len(arr)):
            swap(arr, idx, j)
            _permHelper(arr, permutation, idx + 1)
            swap(arr, idx, j)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


arr = [1, 2, 3]
# print(getPermutation(arr))

# -------------------------------------------------------------#


def powSets(arr):
    subSet = [[]]
    for ele in arr:
        for i in range(len(subSet)):
            currSet = subSet[i]
            subSet.append(currSet + [ele])
    return subSet


arr = [1, 2, 3, 4]
print(powSets(arr))
