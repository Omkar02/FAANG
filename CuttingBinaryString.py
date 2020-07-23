import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


'''
Given a string s containing 0's and 1's. You have to return a smallest positive integer C,
such that the binary string can be cut into C pieces and each piece should be of the power of 5  with no leading zeros.

Input:
The first line of the input contains T denoting the number of test cases. For each test case, there is a string s.

Output:
For each test case, the output is an integer C. If no such cuts are possible then return -1.
'''


string = '101101101'
string = '1111101'
# string  = '00000'

import math

# O(1) | O(1) -------|


def isToThePower(string, power):
    if string == '':
        return False
    return int(string, 2) in power


def cutBinary(string):
    idx = 0
    allOnes = []
    cuts = 0

    allPower = [int(math.pow(5, x)) for x in range(len(string) - 1)]
    idxCheck = []
    # print(allPower)

    # O(n*nlog(x)) -------|
    while idx < len(string) - 1:
        if string[idx] == '1':
            allOnes.append(idx)
        idx += 1
    # print(allOnes)
    for i in allOnes:
        j = len(string)
        print('-------------------')
        while j > i:
            newBin = string[i:j]
            print(i, j, newBin)
            if isToThePower(newBin, allPower) and j not in idxCheck:
                print(newBin, '+++++++++')
                idxCheck.append(j)
                cuts += 1
                break
            j -= 1

        if j == len(string):
            break
    print(cuts)


cutBinary(string)
