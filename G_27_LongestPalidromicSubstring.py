import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')




# odd = =aba
# even = abba

# O(N^2) time | O(1) space
def longestPaliSubstring(string):
    currLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getPali(string, i - 1, i + 1)
        even = getPali(string, i - 1, i)

        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currLongest = max(currLongest, longest, key=lambda x: x[1] - x[0])

    return currLongest, string[currLongest[0]:currLongest[1]]


def getPali(string, left, right):
    while left > 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left + 1, right]


string = 'abaxyzzyxf'
string = "babad"

print(longestPaliSubstring(string))
