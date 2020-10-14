# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def hIndex(citations):
    citations.sort()
    maxCtation = float("-inf")
    n = len(citations)
    for idx, ci in enumerate(citations):
        if ci >= n - idx:
            print(idx, ci, n - idx - 1)
            maxCtation = max(maxCtation, n - idx)

    return maxCtation


citations = [3, 0, 6, 1, 5]
print(hIndex(citations))
