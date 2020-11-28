import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def gAnagram(strs):
    if not strs:
        return [[""]]
    group = {}
    for i in strs:
        currS = ''.join(sorted(i))
        if currS not in group:
            group[currS] = []
        group[currS].append(i)
    return [val for val in group.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ""
print(gAnagram(strs))
