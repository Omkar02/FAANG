# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxSubArrayPartition(string):
    d = {string[i]: i for i in range(len(string))}
    print(d)
    currPos = 0
    o = []
    for idx, letter in enumerate(string):
        currPos = max(currPos, d[letter])
        if currPos == idx:
            o.append(idx)
    return o


string = "ababcbacadefegdehijhklij"
print(maxSubArrayPartition(string))
