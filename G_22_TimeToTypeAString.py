import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def getTimeToType(words, keywords):
    keyWeights = {char: dist for dist, char in enumerate(keywords)}
    # print(keyWeights)
    totalTime = 0
    currCharacter = 0
    for character in words:
        if character not in keyWeights:
            return -1
        totalTime += abs(keyWeights[character] - currCharacter)
        currCharacter = keyWeights[character]

    return totalTime


words = 'cbe'
keywords = "abcdefghijklmnopqrstuvwxy"

print(f'Total Time = {getTimeToType(words,keywords)}')
