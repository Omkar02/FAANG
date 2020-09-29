# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def uniqueAbrivation(wordList):
    isUnique = {}
    for word in wordList:
        n = len(word) - 1
        abr = word[0] + str(len(word[1:n])) + word[n]
        if abr not in isUnique:
            isUnique[abr] = [0, word]
        isUnique[abr][0] += 1

    return [x for x in isUnique.values() if x[0] == 1]


wordList = ["deer", "door", "cake", "card"]
print(uniqueAbrivation(wordList))
