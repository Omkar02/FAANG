# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def wordLadder(beginWord, endWord, wordList):
    q = [[beginWord, [beginWord]]]
    while q:
        node, path = q.pop(0)
        for nxtNode in getNextNode(node, wordList) - set(path):
            if nxtNode == endWord:
                return f'Length = {len(path)+1} | path = {path+[endWord]}'
            q.append([nxtNode, path + [nxtNode]])

    return None


def getNextNode(word, wordList):
    nxtNode = set()
    for w in wordList:
        mismatchCount, length = 0, len(w)
        for idx in range(length):
            if word[idx] != w[idx]:
                mismatchCount += 1
        if mismatchCount == 1:
            nxtNode.add(w)

    return nxtNode


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordLadder(beginWord, endWord, wordList))
