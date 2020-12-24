# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

cnt = [0]


def pali_substring(s):
    cache = {}
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            currS = s[i:j]
            if is_pali(currS):
                count += 1
    return count


def is_pali(s):
    cnt[0] += 1
    return s == s[::-1]


s = "abc"
s = 'aaa'
s = 'aaaaaaaaaaaaaaaaaaaaaaaaa'
s = 'dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg'
print(pali_substring(s))
print(cnt)
