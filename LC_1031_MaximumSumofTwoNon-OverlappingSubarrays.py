# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxSumTwoNoOverlap(A, L, M):
    visited = [9]

    result = sumsOverlay(A, L, visited)
    # result = 0
    result += sumsOverlay(A, M, visited)

    return result


def maxSumTwoNoOverlap(A, L, M):
    print(A)
    for i in range(1, len(A)):  # xrange -> range by Hiro
        A[i] += A[i - 1]

    print(A)
    res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
    print(res, Lmax, Mmax)
    for i in range(L + M, len(A)):  # xrange -> range by Hiro
        Lmax = max(Lmax, A[i - M] - A[i - L - M])
        Mmax = max(Mmax, A[i - L] - A[i - L - M])
        res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
    return res


A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
L = 1
M = 2

print(maxSumTwoNoOverlap(A, L, M))
