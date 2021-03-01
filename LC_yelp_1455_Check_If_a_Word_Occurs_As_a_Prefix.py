# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def isPrefix(sentence, searchWord):
    sentence = sentence.split()
    for idx, word in enumerate(sentence):
        if len(searchWord) < len(word):
            if word[0:len(searchWord)] == searchWord:
                return idx + 1
    return -1


sentence = "i love eating burger"
searchWord = "burg"

# sentence = "this problem is an easy problem"
# searchWord = "pro"

# sentence = "i am tired"
# searchWord = "you"
print(isPrefix(sentence, searchWord))
