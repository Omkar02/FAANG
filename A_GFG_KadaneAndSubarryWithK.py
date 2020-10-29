# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kadens(array):
    maxSum = float('-inf')
    currSum = 0
    startIdx = 0
    endIdx = 0
    n = len(array)
    for i in range(n):
        currSum += array[i]
        if currSum > maxSum:
            maxSum = currSum
            endIdx = i

        if currSum < 0:
            currSum = 0
            startIdx = i

    return maxSum, array[startIdx:endIdx]


array = [-2, -3, 4, -1, -2, 1, 5, -3]

# print(kadens(array))


def SubArray(array):
    array.sort()
    startIdx = 0
    endIdx = 0
    n = len(array)
    currSum = 0
    answer = False
    s = []
    for i in range(n):
        currSum += array[i]
        endIdx += 1
        print(currSum)
        if currSum == 0:
            answer = True
            s.append((startIdx, endIdx))

    return answer, s


array = [4, 2, -3, 1, 6]
# print(SubArray(array))


def binarySerch(array, target):
    l = 0
    r = len(array)
    cnt = 0
    while l <= r:
        piviot = (l + r) // 2
        print(array[piviot])
        if array[piviot] == target:
            return piviot
        elif array[piviot] >= target:
            r = piviot - 1
        else:
            l = piviot + 1
        cnt += 1
        if cnt == 30:
            print(1)
            break
    return -1


array = [3, 4, 15, 20, 30, 70, 80, 120]
# print(binarySerch(array, 70))


def waterArea(heights):
    n = len(heights)
    maxes = [0 for _ in heights]

    leftMax = 0
    for i in range(n):
        he = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, he)

    rightMax = 0
    for i in reversed(range(n)):
        he = heights[i]
        minHeight = min(rightMax, maxes[i])
        if he < minHeight:
            maxes[i] = minHeight - he
        else:
            maxes[i] = 0
        rightMax = max(rightMax, he)

    return sum(maxes)


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(waterArea(arr))


"First one"


def goodNumber(n, k):
    if n < 0:
        return
    n = int(n % (math.pow(10, 9) + 7))
    cnt = 0

    limit = 100000
    for i in range(n, limit):
        totalSum = sum(list(map(int, [i for i in str(i)])))
        if totalSum % 5 == 0:
            cnt += 1
        if k == cnt and i > n:
            return i
    return


import math

# print(goodNumber(6, 5))


def getCountK(n, k):
    cnt = 0
    for i in range(n):
        tSum = sum(map(int, [i for i in str(i)]))
        if tSum % k == 0:
            cnt += 1

    return cnt


# print(getCountK(20, 4))


def mirio(n, m, d, a):
    counts = 0
    curr = 0
    dist = 0
    for i in range(n):
        fa = True
        jump = curr
        for j in reversed(range(d)):
            jump += j + d

            if jump in a:
                curr = jump
            else:
                break

        if jump >= n:
            break

        if fa:
            counts += 1

    return counts
    #     print(dist)
    #     if dist >= n and dist not in a:
    #         return counts
    # return -1


# print(mirio(7, 4, 4, [4, 6, 7]))
# print(mirio(10, 3, 4, [2, 5, 10]))


def findMinimumAdjacentSwaps(arr, N):

    # visited array to check if value is seen already
    visited = [False] * (N + 1)

    minimumSwaps = 0

    for i in range(2 * N):

        # If the arr[i] is seen first time
        if (visited[arr[i]] == False):
            visited[arr[i]] = True

            # stores the number of swaps required to
            # find the correct position of current
            # element's partner
            count = 0

            for j in range(i + 1, 2 * N):

                # Increment count only if the current
                # element has not been visited yet (if is
                # visited, means it has already been placed
                # at its correct position)
                if (visited[arr[j]] == False):
                    count += 1

                # If current element's partner is found
                elif (arr[i] == arr[j]):
                    minimumSwaps += count

    return minimumSwaps


array = [1, 2, 1, 2]
# array = [2, 1, 2, 1]
# array = [1, 2, 2, 1]
# array = [1, 1, 2, 2]
array = [1, 2, 2, 4, 5]
print(findMinimumAdjacentSwaps(array, len(array) // 2))
