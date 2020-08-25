import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
# Time from [1,1] to [3,4] = 3 seconds
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds

import time


def minTimeToVisitAllPoints(points):
    currPos = points[0]
    steps = 0
    cnt = 0
    for endPos in points:
        # print(endPos, 1)
        while currPos != endPos:
            print(f'{currPos}', end='-->')
            cnt += 1
            if endPos[0] <= 0 and endPos[1] >= 0 or endPos[0] >= 0 and endPos[1] <= 0:
                if currPos[0] > endPos[0] and currPos[1] > endPos[1]:
                    steps += 1
                    currPos = [currPos[0] - 1, currPos[1] - 1]

                elif currPos[0] > endPos[0]:
                    steps += 1
                    currPos = [currPos[0] - 1, currPos[1]]

                else:
                    steps += 1
                    currPos = [currPos[0], currPos[1] - 1]

            else:
                if currPos[0] < endPos[0] and currPos[1] < endPos[1]:
                    steps += 1
                    currPos = [currPos[0] + 1, currPos[1] + 1]

                elif currPos[0] > endPos[0]:
                    steps += 1
                    currPos = [currPos[0] + 1, currPos[1]]

                else:  # if currPos[1] > endPos[1]:
                    steps += 1
                    currPos = [currPos[1], currPos[1] + 1]

            if cnt == 100:
                break
        if cnt == 100:
            break
    print(currPos)
    return steps


points = [[1, 1], [3, 4], [-1, 0]]
points = [[3, 2], [-2, 2]]
points  =[[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
print(minTimeToVisitAllPoints(points))


def rule(A, B):
            return max(abs(A[0] - B[0]), abs(A[1] - B[1]))
        
        sum = 0
        
        for tup1, tup2 in zip(points[:-1], points[1:]):
            sum += rule(tup1, tup2)
        
        return sum