import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# O(n) time | O(n) space

def maxSeqNoAdj(array):
    dp = array[:]
    dp[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i])
    print(dp[-1])



# O(n) time | O(1) space
def maxSeqNoAdjOpt(array):
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


array = [7, 10, 12, 7, 9, 14]
print(maxSeqNoAdjOpt(array))
