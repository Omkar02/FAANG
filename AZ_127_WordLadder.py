# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


cnt = [0]


def ladderLength(beginWord, endWord, wordList):
    q = []
    q.append((beginWord, [beginWord]))
    while q:
        node, path = q.pop(0)
        for nxt in nextNode(node, wordList) - set(path):
            if nxt == endWord:
                return f'Total Len = {len(path)+1} and Paths = {path+[nxt]}'
            else:
                q.append((nxt, path + [nxt]))
    return 0


def nextNode(word, wordList):
    toReturn = set()
    for w in wordList:
        mismatch_count, wLength = 0, len(w)
        for i in range(wLength):
            if word[i] != w[i]:
                mismatch_count += 1
        if mismatch_count == 1:
            toReturn.add(w)

    return toReturn

# def ladderLength(beginWord, endWord, wordList):
#     queue = []
#     queue.append((beginWord, [beginWord]))
#     while queue:
#         node, path = queue.pop(0)
#         for nxt in next_nodes(node, wordList) - set(path):
#             if nxt == endWord:
#                 return len(path) + 1, path + [nxt]
#             else:
#                 queue.append((nxt, path + [nxt]))
#     return 0

# def next_nodes(word, word_list):
#     to_return = set()
#     for w in word_list:
#         mismatch_count, w_length = 0, len(w)
#         for i in range(w_length):
#             cnt[0] += 1
#             if w[i] != word[i]:
#                 mismatch_count += 1
#         if mismatch_count == 1:
#             to_return.add(w)
#     return to_return


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladderLength(beginWord, endWord, wordList))
print(cnt)
