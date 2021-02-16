# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Easy')


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    d1, d2 = {}, {}
    for v, w in zip(s, t):
        if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
            return False
        d1[v], d2[w] = w, v
    return True


s = "egg"
t = "add"

s = "foo"
t = "bar"

s = "badc"
t = "baba"

s = "paper"
t = "title"

s = "a"
t = "a"
print(isIsomorphic(s, t))
