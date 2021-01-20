# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def wordBreakProblem(string, dictionary, tOut, res):
    if not string:
        res.append(tOut)
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        if prefix in dictionary:
            wordBreakProblem(string[i:], dictionary, f'{prefix} {tOut}', res)
    return res


dictionary = ["self", "th", "is", "famous", "Word",
              "break", "b", "r", "e", "a", "k", "br",
              "bre", "brea", "ak", "problem"]

string = "Wordbreakproblem"
print(wordBreakProblem(string, dictionary, '', []))
