# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def reconstructQueue(people):
    ans = []
    for p in sorted(people, key=lambda p: (-1 * p[0], p[1])):
        ans.insert(p[1], p)
    return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# Output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
print(reconstructQueue(people))
