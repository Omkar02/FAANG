# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')

cnt = [0]


def exist(board, word):
    t = tries()
    t.addWords(word)

    visited = [[False for x in row] for row in board]
    result = {word: False}
    for i in range(len(board)):
        for j in range(len(board[0])):
            checkIfExits(board, i, j, t.root, visited, result)

    return result[word]


def checkIfExits(board, i, j, triesNode, visited, result):
    cnt[0] += 1
    if visited[i][j]:
        return
    letter = board[i][j]

    if letter not in triesNode:
        return

    visited[i][j] = True
    triesNode = triesNode[letter]

    if '*' in triesNode:
        result[triesNode['*']] = True

    neighbours = getNeighbours(board, i, j)

    for people in neighbours:
        checkIfExits(board, people[0], people[1], triesNode, visited, result)

    visited[i][j] = False


def getNeighbours(board, i, j):
    neighbours = []

    if i > 0 and j > 0:
        neighbours.append([i - 1, j - 1])

    if i > 0 and j < len(board[0]) - 1:
        neighbours.append([i - 1, j + 1])

    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbours.append([i + 1, j + 1])

    if i < len(board) - 1 and j > 0:
        neighbours.append([i + 1, j - 1])

    if i > 0:
        neighbours.append([i - 1, j])

    if i < len(board) - 1:
        neighbours.append([i + 1, j])

    if j > 0:
        neighbours.append([i, j - 1])

    if j < len(board[0]) - 1:
        neighbours.append([i, j + 1])

    return neighbours


class tries():
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def addWords(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]

        current[self.endSymbol] = word

    def printTries(self):
        print(self.root)


board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]

word = "ABFS"
# t = tries()
# t.addWords(word)

# t.printTries()
print(exist(board, word))
print(cnt)
