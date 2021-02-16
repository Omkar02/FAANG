# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Easy')


def longoestCommonPrefix(strs):
    strs = list(zip(*strs))
    ans = ''
    for s in strs:
        if len(set(s)) == 1:
            ans += s[0]
    return ans if ans else -1


strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
print(longoestCommonPrefix(strs))
