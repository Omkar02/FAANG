# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def KdistinctEnementWithlenK(string, k):
    d = {}
    startIdx = 0
    count = 0

    for i in range(len(string)):
        if string[i] in d:
            d[string[i]] -= 1

        if string[i] not in d:
            d[string[i]] = 1

        if d[string[i]] <= 0:
            del d[string[i]]

        if len(d) == k:
            count += 1
        # print(d)

    return count if count != 0 else 0


string = "abcc"
k = 2
string = "aabab"
k = 3
print(KdistinctEnementWithlenK(string, k))
