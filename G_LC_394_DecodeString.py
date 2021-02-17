# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def decodeString(s):
    return decodeStringHelper(s, idx=0)


# def decodeStringHelper(s, idx):

#     decoded = ""
#     n = len(s)
#     while idx < n:
#         currChar = s[idx]
#         if currChar.isnumeric():
#             while idx + 1 < n and s[idx + 1].isnumeric():
#                 currChar += s[idx + 1]
#                 idx += 1
#             multiplier = int(currChar)
#             subString, idx = decodeStringHelper(s, idx + 2)  # for removing the start brackets
#             decoded += subString * multiplier
#             continue

#         if currChar == ']':
#             break

#         decoded += currChar
#         idx += 1
#     return decoded, idx + 1


def decodeStringHelper(s, idx):
    decoded = ""
    n = len(s)
    while idx < n:
        currChar = s[idx]
        if currChar.isnumeric():
            while s[idx + 1].isnumeric():
                currChar += s[idx + 1]
                idx += 1
            multiplier = int(currChar)
            subString, idx = decodeStringHelper(s, idx + 2)
            decoded += subString * multiplier
            continue

        if currChar == ']':
            break
        decoded += currChar
        idx += 1
    return decoded, idx + 1


s = "3[a]2[bc]"
# s = "1[abc]3[cd]ef"
print(decodeString(s))
