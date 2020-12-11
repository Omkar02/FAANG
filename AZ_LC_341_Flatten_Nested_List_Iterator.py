# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# def flatternList(fList):
#     ans = []
#     for lst in fList:

#     return ans


def flatternList(fList):
    n = len(fList)
    while n > 0:
        a = fList.pop(0)
        if type(a) is list:
            fList += a
        else:
            fList.append(a)
        n -= 1
    return fList


fList = [[1, 1], 2, [1, 1]]
# fList = [[1], [1], [1], [1]]
print(flatternList(fList))
