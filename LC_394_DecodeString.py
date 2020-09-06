# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def decodeString(s):
    return decode(s, idx=0)[0]


def decode(string, idx):
    res = ''

    while idx < len(string):
        currChar = string[idx]

        if currChar.isnumeric():
            while string[idx + 1].isnumeric():

                currChar += string[idx + 1]
                idx += 1

            counts = int(currChar)
            substring, idx = decode(string, idx + 2)

            res += substring * counts

            continue

        if currChar == ']':
            break

        res += currChar
        idx += 1
    return res, idx + 1


# s = "3[a]2[bc]"
# s = "3[a2[c]]"
s = "abc3[cd]xyz"
print(decodeString(s))
