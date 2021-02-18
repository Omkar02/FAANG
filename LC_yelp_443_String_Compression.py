# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def compressString(chars):
    n = len(chars)
    ans = ''
    cnt = 0
    idx = 0
    while idx < n:
        currC = chars[idx]
        cnt = 1
        while idx < n - 1 and chars[idx] == chars[idx + 1]:
            cnt += 1
            idx += 1
        ans += f'{currC}{cnt}'
        idx += 1
    return ans


chars = ["a", "a", "b", "b", "c", "c", "c"]
# chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
chars = ["a", "a", "a", "b", "b", "a","a"]
print(compressString(chars))
