# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')
import itertools

# def expressiveWords(self, S, words):
#     def RLE(S):
#         return zip(*[(k, len(list(grp)))
#                      for k, grp in itertools.groupby(S)])

#     R, count = RLE(S)
#     ans = 0
#     for word in words:
#         R2, count2 = RLE(word)
#         if R2 != R: continue
#         ans += all(c1 >= max(c2, 3) or c1 == c2
#                    for c1, c2 in zip(count, count2))

#     return ans


def expressiveWords(S, words):
    sList, sCount = RunLenggthEncoding(S)
    ans = 0
    for word in words:
        wordList, wordCount = RunLenggthEncoding(word)
        # print(wordList, '|', sList)
        if wordList != sList:
            continue
        # print(word, list(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(sCount, wordCount)))
        ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(sCount, wordCount))
    return ans


def RunLenggthEncoding(S):
    return list(zip(*[(char, len(list(grp))) for char, grp in itertools.groupby(S)]))


S = "heeellooo"
words = ["hello", "hi", "heelloo"]
print(expressiveWords(S, words))
