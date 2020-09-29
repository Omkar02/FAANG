# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


cnt = [0, 0]
# dict approch


def longestPath(lines):
    depthMap = {0: 0}
    maxLen = float('-inf')
    lines = lines.split('\n')
    for line in lines:
        cnt[0] += 1
        path = line.split('\t')[-1]
        depth = len(line) - len(path)

        if '.' in path:
            maxLen = max(maxLen, depthMap[depth] + len(path))

        else:
            depthMap[depth + 1] = depthMap[depth] + len(path) + 1

    return maxLen


# stack approch
# def longestPath(lines):
#     lines = lines.split('\n')
#     stack = []
#     maxLen = float('-inf')
#     for line in lines:
#         path = line.split('\t')
#         depth, name = len(path) - 1, path[-1]

#         while stack and stack[-1][1] >= depth:
#             cnt[1] += 1
#             stack.pop()
#         cnt[1] += 1
#         if not stack:
#             stack.append((len(name), depth))
#         else:
#             stack.append((len(name) + stack[-1][0], depth))

#         if '.' in name:
#             maxLen = max(maxLen, stack[-1][0] + stack[-1][1])

#     return maxLen


def longestPath(lines):
    lines = lines.split('\n')
    stack = []
    maxLen = float('-inf')
    for line in lines:
        path = line.split('\t')
        depth, name = len(path) - 1, path[-1]

        while stack and stack[-1][1] >= depth:
            stack.pop()

        if not stack:
            stack.append((len(name), depth))

        else:
            stack.append((len(name) + stack[-1][0], depth))

        if '.' in name:
            maxLen = max(maxLen, stack[-1][0] + stack[-1][1])
    return maxLen


lines = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(longestPath(lines))
# print(cnt)
