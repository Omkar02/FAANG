# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def compareVersion(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    n1, n2 = len(version1), len(version2)
    if n1 > n2:
        version2 += [0] * (n1 - n2)
        n = n1
    elif n1 < n2:
        version1 += [0] * (n2 - n1)
        n = n2
    else:
        n = n1

    p1 = p2 = 0
    while p1 < n and p2 < n:
        if int(version1[p1]) > int(version2[p2]):
            return 1
        elif int(version1[p1]) < int(version2[p2]):
            return -1
        p1 += 1
        p2 += 1
    return 0


version1 = "1.01"
version2 = "1.001"

# version1 = "0.1"
# version2 = "1.1"
print(compareVersion(version1, version2))
