import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sorting', Difficult='Medium')

"""
Given a word S and a text C. Return the count of the occurences of anagrams of the word in the text.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The description of T test cases follows. The first line of each test case contains a 
text S consisting of only lowercase characters.
The second line contains a word consisting of only lowercase characters.

Output:
print the count of the occurences of anagrams of the word C in the text S.
"""
string = "forxxorfxdofr"
target = "for"

# string = 'aabaabaa'
# target = 'aaba'


def coutAnagram(string, target):
    i = 0
    j = len(target)
    counts = 0

    for i in range(len(string) - j + 1):
        if isAnagram(string[i:i + j]) == "".join(sorted(target)):
            counts += 1
    print(counts)


def isAnagram(string):
    return "".join(sorted(string))


coutAnagram(string, target)
