import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def isomorphicStrings(stringOne, stringTwo):
    if len(stringOne) != len(stringTwo):
        return False

    charMap = {i: None for i in stringOne}
    istaken = {i: False for i in stringTwo}

    for i in range(len(stringOne)):
        currChar = stringOne[i]
        if not charMap[currChar] and not istaken[stringTwo[i]]:
            charMap[currChar] = stringTwo[i]
            istaken[stringTwo[i]] = True
        if charMap[currChar] != stringTwo[i]:
            return False
    return True


stringOne = 'paper'
stringTwo = 'title'
print(isomorphicStrings(stringOne, stringTwo))
