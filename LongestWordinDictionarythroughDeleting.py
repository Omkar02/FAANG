import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Medium')


'''G
iven a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. 
If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, 
return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"


'''


def findLongestWord(s, d):
    d.sort(key=lambda x: (-len(x), x))
    for word in d:
        i = j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(word):
            return word
    return ''


s = "ambopnckpelyea"
d = ["ale", "apple", "monskey", "plea"]
print(findLongestWord(s, d))
