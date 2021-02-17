# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def decodeString(s, idx):
    decoded = ""
    n = len(s)
    while idx < n:
        currChar = s[idx]
        if currChar.isnumeric():
            while s[idx + 1].isnumeric():
                currChar += s[idx + 1]
                idx += 1

            multiplier = int(currChar)
            subString, idx = decodeString(s, idx + 2)
            decoded += subString * multiplier
            continue
        if currChar == ']':
            break
        decoded += currChar
        idx += 1
    return decoded, idx + 1


s = "3[a]2[bc]"
print(decodeString(s, 0))
