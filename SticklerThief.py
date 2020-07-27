import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# Stickler the thief wants to loot money from a society having n houses in a single line. He is
#     a weird person and follows a certain rule when looting the houses.
# According to the rule, he will never loot two consecutive houses.
# At the same time, he wants to maximize the amount he loots. The thief knows
# which house has what amount of money but is unable to come up with an optimal looting strategy.
# He asks for your help to find the maximum money he can get if he strictly follows the
# rule. Each house has a[i] amount of money present in it.

# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases
# follow. Each test case contains an integer n which denotes the number of
# houses. Next line contains space separated numbers denoting the amount of money in each house.


def thiefWithRule(array):
    incl = 0
    excl = 0

    for i in array:
        new_excl = max(incl, excl)
        incl = excl + i
        excl = new_excl

    return max(incl, excl)


array = [5, 5, 10, 100, 10, 5]
print(thiefWithRule(array))
