import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# Given an array of integers where each element represents the max number
#  of steps that can be made forward from that element. Write a function to
#  return the minimum number of jumps to reach the end of the array
#  (starting from the first element). If an element is 0, then we cannot move through that element.

# # Examples:

# Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 8 -> 9)
# Explanation: Jump from 1st element to
# 2nd element as there is only 1 step,
# now there are three options 5, 8 or 9.
# If 8 or 9 is chosen then the end node 9
# can be reached. So 3 jumps are made.

# Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# Output: 10
# Explanation: In every step a jump is
# needed so the count of jumps is 10.


# def minJumps(array):
#     # position = [None for x in array]
#     maxReach = array[0]
#     steps = array[0]
#     # position[0] = array[0]
#     jumps = 0

#     for i in range(1, len(array)):
#         maxReach = max(maxReach, array[i] + i)
#         steps -= 1
#         if steps == 0:
#             jumps += 1
#             steps = maxReach - i
#             # position[i] = array[i] + 1
#     # print(position)
#     return jumps + 1


def minJumps(array):
    steps = array[0]
    maxReach = array[0]
    jumps = 0

    for i in range(1, len(array)):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i

    return jumps + 1


array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(array))
