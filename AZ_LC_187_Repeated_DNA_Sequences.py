# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def findRepeatedDnaSequences(s):
    isRepeated = {}
    ans = set()
    for i in range(len(s) - 9):
        currVal = s[i:i + 10]
        if currVal not in isRepeated:
            isRepeated[currVal] = 0
        isRepeated[currVal] += 1

        if isRepeated[currVal] > 1:
            ans.add(currVal)
    return ans


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))
