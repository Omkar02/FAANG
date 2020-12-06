# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def isTherePartten(s):
    n = len(s) // 2 + 1
    for i in range(1, n):
        print(s[:i], s[i:])
        if s == s[:i] + s[i:]:
            # return True
            continue
    return False


s = "abab"
s = "abcabcabcabc"
print(isTherePartten(s))
