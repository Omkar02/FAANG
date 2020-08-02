import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def wordBreak(dictionary, string):
    dp = [[-1 for i in range(len(string))]for i in range(len(string))]

    for frame in range(1, len(string) + 1):
        for i in range(0, len(string) - frame + 1):
            j = i + frame - 1
            subString = string[i:j + 1]

            if subString in dictionary:
                dp[i][j] = i
                continue

            for k in range(i + 1, j + 1):
                if dp[i][k - 1] != -1 and dp[k][j] != -1:
                    dp[i][j] = k
                    break
            [print(x) for x in dp]
            print()
    if dp[0][-1] == -1:
        return None

    words = []
    startIdx = 0
    endIdx = len(string) - 1
    while startIdx < len(string):
        splitIdx = dp[startIdx][endIdx]
        if startIdx == splitIdx:
            words.append(string[startIdx:endIdx + 1])
            break
        else:
            words.append(string[startIdx:splitIdx])

        startIdx = splitIdx

    return " ".join(words)


dictionary = {"joy", "likes", "to", "play"}
string = "joylikestoplay"
print(wordBreak(dictionary, string))
