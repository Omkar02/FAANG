import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]


def groupAnagram(listOfWords):
    group = {}

    for i in listOfWords:
        sortedCurrWord = ''.join(sorted(i))
        if sortedCurrWord not in group:
            group[sortedCurrWord] = [i]

        else:
            group[sortedCurrWord].append(i)
    return [x for k, x in group.items()]


listOfWords = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(listOfWords))
