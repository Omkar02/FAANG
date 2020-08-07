class maxHeap():
    def __init__(self, arr):
        self.heap = self.buildHeap(arr)
        self.length = 0

    def buildHeap(self, arr):
        parentIdx = (len(arr) - 1) // 2
        for currIdx in reversed(range(parentIdx)):
            self.shiftDown(currIdx, len(arr) - 1, arr)
        return arr

    def shiftDown(self, currIdx, endIdx, heap):
        lChild = 2 * currIdx + 1
        while lChild <= endIdx:
            rChild = 2 * currIdx + 2 if currIdx * 2 + 2 <= endIdx else -1
            if rChild != -1 and heap[rChild] > heap[lChild]:
                idxtoSwap = rChild
            else:
                idxtoSwap = lChild
            if heap[idxtoSwap] > heap[currIdx]:
                self.swap(currIdx, idxtoSwap, heap)
                currIdx = idxtoSwap
                lChild = currIdx * 2 + 1
            else:
                break

    def ShiftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] > heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valtoRemove = self.heap.pop()
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return valtoRemove

    def insert(self, val):
        self.heap.append(val)
        self.ShiftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def printHeap(self):
        print(self.heap)


''' 
    -----------------Min_haep--------------------------------------------
'''


class minHeap():
    def __init__(self, arr):
        self.heap = self.buildHeap(arr)
        self.length = 0

    def buildHeap(self, arr):
        parentIdx = (len(arr) - 1) // 2
        for currIdx in reversed(range(parentIdx)):
            self.shiftDown(currIdx, len(arr) - 1, arr)
        return arr

    def shiftDown(self, currIdx, endIdx, heap):
        lChild = 2 * currIdx + 1
        while lChild <= endIdx:
            rChild = 2 * currIdx + 2 if currIdx * 2 + 2 <= endIdx else -1
            if rChild != -1 and heap[rChild] < heap[lChild]:
                idxtoSwap = rChild
            else:
                idxtoSwap = lChild
            if heap[idxtoSwap] < heap[currIdx]:
                self.swap(currIdx, idxtoSwap, heap)
                currIdx = idxtoSwap
                lChild = currIdx * 2 + 1
            else:
                break

    def ShiftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valtoRemove = self.heap.pop()
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return valtoRemove

    def insert(self, val):
        self.heap.append(val)
        self.ShiftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def printHeap(self):
        print(self.heap)
