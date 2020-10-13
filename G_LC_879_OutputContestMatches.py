# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

"""https://www.lintcode.com/problem/output-contest-matches/description"""

import sys


def matchesSchdule(n):
    teams = [i for i in range(1, n + 1)]
    print(teams)
    return helper(teams, 0, n)


def helper(match, i, n):
    if i == 30:
        sys.exit()
    matches = []
    l, r = 0, len(match) - 1

    if l == r:
        return match[0]
    while l <= r:
        matches.append((match[l], match[r]))
        l += 1
        r -= 1
    return helper(matches, i + 1, n)


n = 6
print(matchesSchdule(n))
