# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def wordLadder(beginWord, endWord, wordList):
    # q = [[currNode,[path]]]
    q = [[beginWord, [beginWord]]]
    while q:
        currNode, path = q.pop(0)
        for nxtNode in getNextNode(currNode, wordList) - set(path):
            if nxtNode == endWord:
                return path + [endWord]
            q.append([nxtNode, path + [nxtNode]])
    return None


def getNextNode(word, wordList):
    nxtNode = set()
    for w in wordList:
        mismatchCount, n = 0, len(w)
        for idx in range(n):
            if w[idx] != word[idx]:
                mismatchCount += 1
        if mismatchCount == 1:
            nxtNode.add(w)
    return nxtNode


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordLadder(beginWord, endWord, wordList))
