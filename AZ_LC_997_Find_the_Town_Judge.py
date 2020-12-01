# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Easy')


def findJudge(n, trust):
    relation = {a: [] for a in range(1, n + 1)}
    for i in trust:
        relation[i[0]].append(i[0])

    for i in range(1, n + 1):
        if not relation[i]:
            return i
    return -1


n = 2
trust = [[1, 2]]

n = 3
trust = [[1, 3], [2, 3]]

n = 3
trust = [[1, 3], [2, 3], [3, 1]]

n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(findJudge(n, trust))
