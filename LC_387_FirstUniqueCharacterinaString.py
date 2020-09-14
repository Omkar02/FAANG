# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def firstUniqChar(s):
    visited = {}
    for idx, i in enumerate(s):
        if i not in visited:
            visited[i] = (idx, True)
        else:
            visited[i] = (idx, False)

    minIndex = float('inf')

    for idx, i in enumerate(s):
        curr = visited[i]
        if curr[1]:
            minIndex = min(minIndex, curr[0])

    return minIndex


s = 'leetcode'
s = 'loveleetcode'
print(f'The Index of Unique char is {firstUniqChar(s)}')
