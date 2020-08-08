import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tries', Difficult='Medium')


# The Question:
# There is a broken keyboard in which space gets typed when you type the letter 'e'. Given an input string which is the output from the keyboard.
# A dictionary of possible words is also provided as an input parameter of the method. Return a list of possible actual input typed by the user.

class Tries():
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def addWord(self, words):
        current = self.root
        for letter in words:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = words

    def getRoot(self):
        return self.root


String = "can s r n "
Dictionary = {"can", "canes", "serene", "rene", "sam"}

# Expected Output: ["can serene", "canes rene"]
# print(String[len(String) - 1])


def brokenKeyboard(String, Dictionary):
    tries = Tries()
    answer = []
    root = tries.getRoot()
    for words in Dictionary:
        tries.addWord(words)
    # tries.printTries()
    brokenKeyboardHelper(String, Dictionary, answer, [], root, 0, root)
    return answer


def brokenKeyboardHelper(String, Dictionary, answer, currSentence, currtries, index, root):
    # print(currtries, '-------------------', root)
    if index == len(String):
        if currtries == root:
            answer.append(' '.join(currSentence))
        elif '*' in currtries:
            answer.append(' '.join(currSentence) + ' ' + currtries['*'])
        return

    currChar = String[index]
    if currChar.isalpha() and currChar in currtries:
        brokenKeyboardHelper(String, Dictionary, answer, currSentence, currtries[currChar], index + 1, root)

    if currChar == ' ' and '*' in currtries:
        currSentence.append(currtries['*'])
        brokenKeyboardHelper(String, Dictionary, answer, currSentence, root, index + 1, root)
        currSentence.pop()

    if currChar == ' ' and 'e' in currtries:
        brokenKeyboardHelper(String, Dictionary, answer, currSentence, currtries['e'], index + 1, root)


print(brokenKeyboard(String, Dictionary))
