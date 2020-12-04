# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def wordPartten(word, partten):
    word = word.split()

    if len(word) != len(partten):
        return False

    charMap = {}
    for idx, val in enumerate(zip(word, partten)):
        w, p = val
        if w not in charMap:
            charMap[w] = idx
        if p not in charMap:
            charMap[p] = idx
        if charMap[w] != charMap[p]:
            return False
    return True


partten = "abba"
word = "dog cat cat dog"

partten = "aaba"
word = "dog dog dog dog"
print(wordPartten(word, partten))
