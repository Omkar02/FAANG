# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def alphabeticalOrder(String):
    n = len(String)
    if n == 0:
        return 0
    split = 1
    i = 0

    while i < n:
        split += 1

        while i + 1 < n and String[i] <= String[i + 1]:
            i += 1
        while i + 1 < n and String[i] >= String[i + 1]:
            i += 1

        i += 1
    return split


String = 'abcdcba'
# String = 'gfcbdhdd'
# String = 'hcbehahccaag'
print(f'Split = {alphabeticalOrder(String)}')

def goodSubString(s):

    if not s:
        return 0
    subStrings = 0
    flagRev = 2  # 0 for increse, 1 for Dec, 2 for startMode

    for i in range(len(s) - 1):

        if s[i] > s[i + 1]:

            if flagRev == 1:
                subStrings = subStrings + 1
                flagRev = 2
            else:
                flagRev = 0

        elif s[i] < s[i + 1]:

            if flagRev == 0:
                subStrings = subStrings + 1
                flagRev = 2
            else:
                flagRev = 1
    return subStrings + 1


print(f'Split = {goodSubString(String)}')
