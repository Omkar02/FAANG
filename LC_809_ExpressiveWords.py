import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def ExpreciceWords(word, dictionary):
    wordCnt = {x: word.count(x) for x in set(word)}
    print(wordCnt)
    for checkToMake in dictionary:
        for key, val in wordCnt.items():
            thatsIt = False
            print(checkToMake.count(key), wordCnt[key], checkToMake.count(key), key)
            if checkToMake.count(key) == wordCnt[key] or wordCnt[key] >= 3:
                thatsIt = True

        if thatsIt:
            return checkToMake


word = "heeellooo"
dictionary = ["hello", "hi", "helo"]

print(ExpreciceWords(word, dictionary))
