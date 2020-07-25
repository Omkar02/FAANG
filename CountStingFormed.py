import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


"""
Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’ 
with at-most one ‘b’ and two ‘c’s allowed.

Input:
The first line of input contains an integer T denoting the number of test cases. T
hen T test cases follow. The first line of each test case contains an integer N denoting the length of the string.

Output:
Output the count of the strings that can be formed under the given constraint.

Input:
2
1
3

Output:
3
19
"""

times = [0]


def countTheString(n, cCount, bCount, cache):
    print(n, bCount, cCount, '-----', times)
    times[0] += 1

    if (n, bCount, cCount) in cache:
        print('@----hit----@')
        return cache[(n, bCount, cCount)]

    if cCount < 0 or bCount < 0:
        return 0
    if n == 0:
        return 1
    if bCount == 0 and cCount == 0:
        return 1

    result = countTheString(n - 1, cCount, bCount, cache)
    result += countTheString(n - 1, cCount - 1, bCount, cache)
    result += countTheString(n - 1, cCount, bCount - 1, cache)

    cache[(n, bCount, cCount)] = result
    return result


sLength = 3
print(countTheString(sLength, 1, 2, {}))
