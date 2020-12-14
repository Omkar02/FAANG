# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def rconstructIp(s):
    res = []
    buildIP(s, '', 0, res)
    return res


def buildIP(s, prefix, integers, res):
    if not s:
        if integers == 4:
            res.append(prefix)

    if integers > 3:
        return

    period = '.' if integers < 3 else ''
    buildIP(s[1:], prefix + s[0] + period, integers + 1, res)

    if 9 < int(s[0:2]) < 100:
        buildIP(s[2:], prefix + s[0:2] + period, integers + 1, res)
    if 99 < int(s[0:3]) < 256:
        buildIP(s[3:], prefix + s[0:3] + period, integers + 1, res)


s = "25525511135"
print(rconstructIp(s))
