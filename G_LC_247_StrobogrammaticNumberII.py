# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')

"""
0 after 180° rotation : (0 → 0)
1 after 180° rotation : (1 → 1)
8 after 180° rotation : (8 → 8)
6 after 180° rotation : (6 → 9)
9 after 180° rotation : (9 → 6)
"""


# # strobogrammatic function
# def strobogrammatic_num(n):

#     result = numdef(n, n)
#     return result

def strobogrammaticNum(n):
    return strobogrammaticHelper(n, length=n)


def strobogrammaticHelper(n, length):
    if not n:
        return [""]
    if n == 1:
        return ["1", "0", "8"]

    mid = strobogrammaticHelper(n - 2, length)
    res = []
    for mPoints in mid:
        if n != length:
            res.append("0" + mPoints + "0")
        res.append("8" + mPoints + "8")
        res.append("1" + mPoints + "1")
        res.append("9" + mPoints + "6")
        res.append("6" + mPoints + "9")

    return res


n = 2
print(strobogrammaticNum(n))
