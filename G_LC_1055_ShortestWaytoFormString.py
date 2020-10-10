# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def shotestWaytoFormString(scr, target):
    numMinString = 0
    remaning = target
    while len(remaning) != 0:
        subsequence = ""
        i = j = 0
        while i < len(scr) and j < len(remaning):
            if scr[i] == remaning[j]:
                subsequence += remaning[j]
                j += 1
            i += 1

        if len(subsequence) == 0:
            return -1

        numMinString += 1
        remaning = remaning[len(subsequence):]
    return numMinString


scr = "abc"
target = "abcbc"

scr = "abc"
target = "abcdbc"
a = [1, 2, 3, 4, 5]

print(shotestWaytoFormString(scr, target))
