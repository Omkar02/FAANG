import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]
CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')


'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [0, 2]


def maxArea(height):
    largest = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        largest = max(largest, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return largest


print(maxArea(height))
