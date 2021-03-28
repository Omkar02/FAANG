import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


from Datastruct.masterLinkedList import l, v, r


a = [7, 2, 4, 3]
b = [5, 6, 4]

[l.insertStart(x) for x in a]
[v.insertStart(x) for x in b]

# v.traverseList()


def addTwoNum(a, b):
    s1, s2 = '', ''
    while a:
        s1 += str(a.data)
        a = a.nextNode

    while b:
        s2 += str(b.data)
        b = b.nextNode

    totalSum = str(int(s1) + int(s2))
    [r.insertStart(x) for x in totalSum]
    r.traverseList()


# print(addTwoNum(l.getHead(), v.getHead()))

def isValid(brackets):
    if not brackets:
        return False
    mapping = {')': '(',
               ']': '[',
               '}': '{'}

    openingBracket = '({['
    closingBracket = ')}]'

    stack = []
    for i in brackets:
        if i in openingBracket:
            stack.append(i)
        if i in closingBracket:
            if not stack:
                return False
            if stack[-1] == mapping[i]:
                stack.pop()
    return len(stack) == 0


brackets = ''
# print(isValid(brackets))


def minPathSum(grid):
    rLen = len(grid)
    cLen = len(grid[0])

    dp = [[0 for _ in c] for c in grid]

    dp[0][0] = grid[0][0]

    for i in range(1, cLen):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    for i in range(1, rLen):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, rLen):
        for j in range(1, cLen):
            dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
    [print(x) for x in dp]

    return dp[-1][-1]


grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]

# grid = [[1, 2, 3],
#         [4, 5, 6]]
print(minPathSum(grid))
