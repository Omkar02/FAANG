# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def quickSelect(arr, k):
    postion = k - 1
    return _quickHelp(arr, 0, len(arr) - 1, postion)


def _quickHelp(arr, lo, hi, postion):
    while lo < hi:
        piv = lo
        lIdx = lo + 1
        rIdx = hi
        while lIdx <= rIdx:
            if arr[lIdx] < arr[rIdx] and arr[rIdx] > arr[piv]:
                swap(arr, lIdx, rIdx)

            if arr[lIdx] >= arr[piv]:
                lIdx += 1
            if arr[rIdx] <= arr[piv]:
                rIdx -= 1
        swap(arr, rIdx, piv)

        if rIdx == postion:
            return arr[rIdx]
        elif rIdx > postion:
            hi = rIdx - 1
        else:
            lo = rIdx + 1


def swap(a, s, o):
    a[s], a[o] = a[o], a[s]


arr = [2, 3, 5, 6, 7, 8, 9]
arr = [1, 2, 3]
k = 3
print(quickSelect(arr, k))
