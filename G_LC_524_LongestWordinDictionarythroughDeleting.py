# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findLongestWord(s, d):
    d.sort(key=lambda a: (-len(a), a))
    for word in d:
        i = j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if len(word) == j:
            return word
    return ""


s = "abpcplkea"
d = ["ale", "apple", "monkey", "plea"]
s = "bab"
d = ["ba", "ab", "a", "b"]
print(findLongestWord(s, d))
