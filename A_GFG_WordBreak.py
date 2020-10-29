# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tries', Difficult='Hard')


class wordBreak:
    def __init__(self, dictionary, string):
        self.tries = {}
        self.endWord = '*'
        self.ans = []
        self.addWord(dictionary)
        self.brWord(string)

    def addWord(self, wordList):
        for words in wordList:
            curr = self.tries
            for character in words:
                if character not in curr:
                    curr[character] = {}
                curr = curr[character]
            curr[self.endWord] = words

    def brWord(self, string):
        currNode = self.tries
        for char in string:
            if char not in currNode:
                currNode = self.tries

            if char not in currNode:
                self.ans.append(False)
                continue
            currNode = currNode[char]
            if '*' in currNode:
                self.ans.append(currNode['*'])


# dictionary = ["the", "quick", "fox", "brown"]
# string = 'thequickbrownfox'

dictionary = ["bed", "bath", "bedbath", "and", "away"]
# dictionary = ["teddy", "bath", "bedbath", "and", "beyond"]
string = 'bedbathandbeyond'
w = wordBreak(dictionary, string)
print(w.ans)
print(w.tries)
