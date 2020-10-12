# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Medium')


def canTransform(scr, target):
    if len(scr) != len(target):
        return False

    idx1 = idx2 = 0
    while idx1 < len(scr) and idx2 < len(target):
        if scr[idx1] != target[idx2] and scr[idx1] != 'X' and target[idx2] != 'X':
            return False

        if scr[idx1] == 'X':
            idx1 += 1

        if target[idx2] == 'X':
            idx2 += 1

        idx1 += 1
        idx2 += 1

    return True


scr = "RXXLRXRXL"
target = "XRLXXRRLX"

scr = "LLR"
target = "RRL"
print(canTransform(scr, target))
