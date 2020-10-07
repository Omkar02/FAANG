# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def longestStrChain(words):
    stringChain = {}
    for string in words:
        stringChain[string] = {'nextSting': '', 'maxChainLength': 1}
    words.sort(key=len)
    for string in words:
        findLongestStringChain(string, stringChain)
    return buildLongestStringChain(words, stringChain)


def findLongestStringChain(string, stringChain):
    for i in range(len(string)):
        smallString = getSmallerString(string, i)
        if smallString not in stringChain:
            continue
        tryUpdateLongestString(string, smallString, stringChain)


def getSmallerString(string, idx):
    return string[0:idx] + string[idx + 1:]


def tryUpdateLongestString(currentString, smallString, stringChain):
    smlength = stringChain[smallString]['maxChainLength']
    culength = stringChain[currentString]['maxChainLength']

    if smlength + 1 > culength:
        stringChain[currentString]['maxChainLength'] = smlength + 1
        stringChain[currentString]['nextSting'] = smallString


def buildLongestStringChain(strings, stringChain):
    maxChainLength = 0
    chainStartingString = ''
    for string in strings:
        if stringChain[string]['maxChainLength'] > maxChainLength:
            maxChainLength = stringChain[string]['maxChainLength']
            chainStartingString = string

    ourLongestChain = []
    currentString = chainStartingString
    while currentString:
        ourLongestChain.append(currentString)
        currentString = stringChain[currentString]['nextSting']

    return list(reversed(ourLongestChain))


words = ["a", "b", "ba", "bca", "bda", "bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".

print(longestStrChain(words))
