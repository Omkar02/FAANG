# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tries', Difficult='Hard')


class tries:
    def __init__(self):
        self.root = {}
        self.endWord = '*'

    def addword(self, word):
        current = self.root

        for character in word:
            if character not in current:
                current[character] = {}
            current = current[character]

        current[self.endWord] = word


def findSecretWord(wordlist, secret, guess):
    t = tries()
    for word in wordlist:
        t.addword(word)

    return getTheWord(guess, t.root, 0)


def getTheWord(guess, node, idx):
    # print(idx, len(guess), node)
    if '*' in node:
        return (idx, True)

    if guess[idx] not in node:
        return idx

    node = node[guess[idx]]
    idx += 1

    return getTheWord(guess, node, idx)


secret = "abcdzz"
wordlist = ["acckzz", "ccbazz", "eiowzz", "abcczz"]

print(findSecretWord(wordlist, secret, secret))
