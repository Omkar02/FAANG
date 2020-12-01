# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def longCommonPrefix(strs):
    ans = ''
    for tup in zip(*strs):
        if min(tup) == max(tup):
            ans += tup[0]
        else:
            break

    return ans


strs = ["flower", "flow", "flight"]
print(longCommonPrefix(strs))
