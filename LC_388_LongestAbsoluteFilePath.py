# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
string = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"


def longestAbsPath(input):
    lines = input.split('\n')
    depth_map = {0: 0}
    maxLen = float('-inf')
    for line in lines:
        path = line.split('\t')[-1]

        depth = len(line) - len(path)

        if '.' in path:
            maxLen = max(maxLen, depth_map[depth] + len(path))

        else:
            print(depth_map, depth)
            depth_map[depth + 1] = depth_map[depth] + len(path) + 1

    return maxLen


print(longestAbsPath(string))
