# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Hard')


def kEmptySlots(flowers, k):
    n = len(flowers)
    days = [0] * len(flowers)
    for i in range(len(flowers)):
        days[flowers[i] - 1] = i + 1
    # print(days == flowers)
    res = float('inf')
    i, left, right = 0, 0, k + 1
    while right < n:

        if days[i] < days[left] or days[i] <= days[right]:
            if i == right:
                res = min(res, max(days[left], days[right]))
            left, right = i, i + k + 1
        i += 1
    return -1 if res == float("inf") else res


flowers = [1, 3, 2]
k = 1

print(kEmptySlots(flowers, k))
