# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Heap', Difficult='Medium')

import heapq


class KthLargest():
    def __init__(self, k, nums):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        print(self.heap, val)
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)

        # print('\t|->', self.heap[0], self.heap)
        return self.heap[0]


nums = [4, 5, 8, 2]
k = 6
kLar = KthLargest(k, nums)
kLar.add(4)
kLar.add(10)
kLar.add(9)
kLar.add(3)
