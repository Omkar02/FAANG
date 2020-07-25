import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')

'''
Given two strings, the task is to check whether these strings are meta strings or 
not. Meta strings are the strings which can be made equal by exactly one swap in any 
of the strings. Equal string are not considered here as Meta strings.

Examples:

Input : A = "geeks" 
        B = "keegs"
Output : 1
By just swapping 'k' and 'g' in any of string, 
both will become same.

Input : A = "rsting"
        B = "string
Output : 0
'''

A = "geeks"
B = "keegs"


def metaString(oneSting, twoString):
    if len(oneSting) != len(twoString):
        return 0
    swap = 0
    for i in range(len(oneSting)):
        if oneSting[i] != twoString[i]:
            swap += 1

    return 1 if swap == 2 else 0


print(metaString(A, B))
