# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class WordDictionary:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def addWord(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}

            current = current[letter]
        current[self.endSymbol] = word

    def search(self, word):
        return self._match(self.root, word, 0)

    def _match(self, node, word, idx):
        if len(word) == idx:
            return True

        current = node

        if word[idx] != '.' and word[idx] not in current:
            return False

        if word[idx] != '.':
            return self._match(current[word[idx]], word, idx + 1)

        else:
            for childsNodes in current.values():
                if self._match(childsNodes, word, idx + 1):
                    return True

        return False


arr = ['bad', 'dad', 'dap', 'dda', 'mad', 'pad']
w = WordDictionary()

for i in arr:
    w.addWord(i)

print(w.search('bad'))
