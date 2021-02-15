# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kFreqWords(words, k):
    candidates = {word: words.count(word) for word in set(words)}
    return sorted(candidates, key=lambda a: (-candidates[a], a))[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4

print(kFreqWords(words, k))
