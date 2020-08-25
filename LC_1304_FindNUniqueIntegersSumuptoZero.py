import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].


def sumZero(n):
    res = []
    if n % 2 == 0:
        for i in range(1, n + 1, 2):
            res.append(i)
            res.append(-1 * i)
    else:
        res.append(0)
        for i in range(1, n, 2):
            res.append(i)
            res.append(-1 * i)

    return res


n = 6
print(sumZero(n))
