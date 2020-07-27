import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Mediun')

'''
Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, generate all binary 
strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’.

Input:
The first line of input contains a single integer T, denoting the number of test cases. 
Then T test cases follow. Each test case consist of one line. The first line of each test case consists of a string S.

Output:
Print all binary string that can be formed by replacing each wildcard character.

Constraints:
1 ≤ T ≤ 60
1 ≤ |S| ≤ 30

Example:
Input
1
1??0?101

Output
10000101 10001101 10100101 10101101 11000101 11001101 11100101 11101101
'''


def wildbinarystring(string, idx):
    if idx == len(string) - 1:
        print(''.join(string))
        return
    if string[idx] == '?':
        string[idx] = '1'
        wildbinarystring(string, idx + 1)
        string[idx] = '0'
        wildbinarystring(string, idx + 1)
        string[idx] = '?'
    else:
        wildbinarystring(string, idx + 1)


string = list('1??0?101')
wildbinarystring(string, 0)
