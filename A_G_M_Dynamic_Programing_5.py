# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


"Minimum Jump To Reach End"


def MJRE(jumps):
    n = len(jumps)
    maxReach = steps = jumps[0]
    j = 0
    for i in range(1, n - 1):
        cnt[0] += 1
        steps -= 1
        maxReach = max(maxReach, jumps[i] + i)
        if not steps:
            j += 1
            steps = maxReach - i
        if i >= maxReach:
            return -1
    return j + 1


jumps = [2, 0, 3, 4]
# print(MJRE(jumps))
# print(cnt)


"Minimum Cost Path"


def MCP(board):
    r, c = len(board), len(board[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = board[0][0]
    for i in range(1, c):
        dp[0][i] = dp[0][i - 1] + board[0][i]

    for i in range(1, r):
        dp[i][0] = dp[i - 1][0] + board[i][0]

    for x in range(1, r):
        for y in range(1, c):
            dp[x][y] = board[x][y] + min(dp[x - 1][y - 1],
                                         dp[x - 1][y],
                                         dp[x][y - 1])

    [print(x)for x in dp]

    return dp[-1][-1]


board = [[1, 3, 5, 8],
         [4, 2, 1, 7],
         [4, 3, 2, 3]]
# print(MCP(board))


"Text Justification"


def TJ(words, maxWidth):
    res, cur = [], []
    numOfLetters = 0
    for w in words:
        if numOfLetters + len(w) + len(cur) > maxWidth:
            # print(True)
            # for i in range(maxWidth - numOfLetters):
            #     cur[i % (len(cur) - 1 or 1)] += ' '
            #     print(cur)
            res.append(' '.join(cur))
            cur, numOfLetters = [], 0
        cur += [w]
        numOfLetters += len(w)
    return res + [" ".join(cur)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
# print(TJ(words, maxWidth))


"Optimal Game Strategy"


def OGS(array, i, j, currSum):
    cnt[0] += 1
    if j == i + 1:
        return max(array[i], array[j])
    return max(currSum - OGS(array, i + 1, j, currSum - array[i]),
               currSum - OGS(array, i, j - 1, currSum - array[j]))


array = [8, 15, 3, 7]
array = [20, 30, 2, 2, 2, 10]
# print(OGS(array, 0, len(array) - 1, sum(array)))
# print(cnt)
