# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def replaceTheString(S, indexes, sources, targets):
    S = list(S)
    n = len(S)
    for idx, scr, tar in sorted(zip(indexes, sources, targets), reverse=True):
        # if all(i+k < len(S) and S[i+k] == x[k] for k in range(len(x))):
        if all(idx + k < n and S[idx + k] == scr[k] for k in range(len(scr))):
            S[idx:idx + len(scr)] = list(tar)

    return "".join(S)


S = "abcd"
indexes = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

print(replaceTheString(S, indexes, sources, targets))
