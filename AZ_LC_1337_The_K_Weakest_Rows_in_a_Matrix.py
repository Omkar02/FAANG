# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def weakestRow(feild, k):
    solCount = [(sum(x), i) for i, x in enumerate(feild)]
    solCount.sort()
    count = 0
    ans = []
    for i in solCount:
        if count >= k:
            break
        ans.append(i[1])
        count += 1
    return ans


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3

print(weakestRow(mat, k))
