# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tries', Difficult='Medium')


class Tries:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def addWord(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]

        current[self.endSymbol] = word

    def printTries(self):
        print(self.root)


def ifExist(board, words):
    t = Tries()
    for w in words:
        t.addWord(w)
    t.printTries()
    visited = [[False for x in row]for row in board]
    result = set()

    for r in range(len(board)):
        for c in range(len(board[0])):
            checkIfExits(board, r, c, t.root, visited, result)
    return result


def checkIfExits(board, r, c, node, visited, result):
    if visited[r][c]:
        return

    letter = board[r][c]

    if letter not in node:
        return

    visited[r][c] = True
    node = node[letter]

    if '*' in node:
        result.add(node['*'])

    neighbours = getNeighbours(board, r, c)

    for people in neighbours:
        checkIfExits(board, people[0], people[1], node, visited, result)

    visited[r][c] = False


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


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]


print(ifExist(board, words))
