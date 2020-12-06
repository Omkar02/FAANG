# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')
import string


def verifyAlienDict(words, order):
    alien_dict = {key: val for key, val in zip(order, string.ascii_lowercase)}
    preWord = '!'
    for word in words:
        currWord = ''.join(alien_dict[c] for c in word)
        print(currWord)
        if currWord < preWord:
            return False
        preWord = currWord
    return True


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(verifyAlienDict(words, order))
