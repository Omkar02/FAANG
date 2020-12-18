# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


"""Find the highest index i such that s[i] < s[i+1]. If no such index exists, the permutation is the last permutation.
    Find the highest index j > i such that s[j] > s[i]. Such a j must exist, since i+1 is such an index.
    Swap s[i] with s[j].
    Reverse the order of all of the elements after index i till the last element."""


def nextGreaterEle(n):
    nString = list(str(n))
    p1 = p2 = -1
    nLen = len(nString)
    for i in reversed(range(nLen - 1)):
        if nString[i] < nString[i + 1]:
            """highest index"""
            p1 = i
            break
    if p1 != -1:
        for i in reversed(range(p1, nLen)):
            """highest index from i to p1"""
            if nString[i] > nString[p1]:
                p2 = i
                break
    else:
        return -1
    return finalizedOut(nString, p1, p2)


def finalizedOut(arr, p1, p2):
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    return ''.join(arr)


n = 323
print(nextGreaterEle(n))
