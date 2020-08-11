import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


# Title description
# The count-and-say sequence is the sequence of integers beginning as follows: 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.

# Problem solving method
# Finding out the rule of generating this string is actually counting. If the current charter is equal to the previous one, add 1;
# otherwise, add the current one to the result and start counting from 1 again

cnt = [0]


def speackLoud(n):
    cache = {1: "1"}
    if not n or n == 1:
        return cache[n]

    for i in range(1, n):
        # print(cache)
        currLen = len(cache[i])
        nextstr = ''
        prefix = 1
        for j in range(1, currLen):
            cnt[0] += 1

            # print(cache[i][j], cache[i][j - 1])
            if cache[i][j] == cache[i][j - 1]:
                prefix += 1
            else:
                # print('-----')
                nextstr += str(prefix) + cache[i][j - 1]
                prefix = 1
                # print(nextstr, '=======')
        nextstr += str(prefix) + cache[i][-1]
        cache[i + 1] = nextstr

    return cache[n]


print(speackLoud(8)=='1113213211')
print(cnt)
