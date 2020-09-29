# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def minDominoRotations(A, B):
    if len(A) != len(B):
        return -1

    n = len(A)
    ans = float('inf')

    for i in range(1, 7):
        # print(i)
        c1 = c2 = 0
        for j in range(n):
            if A[j] != i and B[j] == i:
                c1 += 1
            elif A[j] == i and B[j] != i:
                c2 += 1
            elif A[j] == i and B[j] == i:
                continue
            else:
                c1 = c2 = float('inf')
                break

        ans = min(ans, c1, c2)
    return ans if ans != float('inf')else -1


A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]

# A = [3, 5, 1, 2, 3]
# B = [3, 6, 3, 3, 4]

A = [6, 1, 6, 4, 6, 6]
B = [5, 6, 2, 6, 3, 6]


print(minDominoRotations(A, B))
