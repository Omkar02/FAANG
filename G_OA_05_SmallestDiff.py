import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and
# add x to A[i] (only once).

# After this process, we have some array B.

# Return the smallest possible difference between the maximum value of B and the minimum value of B.


# Example 1:

# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:

# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]

# Example 3:

# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
def smallestDiff(array, k):
    maxEle = float('-inf')
    maxEleIdx = 0
    for i in range(len(array)):
        if array[i] > maxEle:
            maxEle = array[i]
            maxEleIdx = i

    diff = []
    for i in range(len(array)):
        if i != maxEleIdx:
            diff.append(array[i] + k)
        else:
            diff.append(array[i] - k)

    return max(diff) - min(diff)


array = [1, 3, 6]
k = 3
print(smallestDiff(array, k))
