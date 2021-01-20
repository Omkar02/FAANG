# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def canTestFitted(words, maxWidth):
    res, cur = [], []
    lenOfWords = 0
    for w in words:
        if len(w) + len(cur) + lenOfWords > maxWidth:
            res.append(' '.join(cur))
            cur, lenOfWords = [], 0
        lenOfWords += len(w)
        cur += [w]
    return res + [' '.join(cur)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(canTestFitted(words, maxWidth))
