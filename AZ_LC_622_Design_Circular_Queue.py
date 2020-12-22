# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


class circular_queue:
    def __init__(self, size):
        self.data = [None for _ in range(size)]
        self.head = 0
        self.tail = 0
        self.qLen = 0

    def enQueue(self, val):
        if self.isFull():
            return False
        self.data[self.tail] = val
        self.tail += 1
        self.qLen += 1

    def deQueue(self):
        if self.isEmpty():
            return False

        self.head += 1
        self.qLen -= 1

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[(self.tail - 1) % len(self.data)]

    def isEmpty(self) -> bool:
        return self.qLen == 0

    def isFull(self) -> bool:
        return self.qLen == len(self.data)


q = circular_queue(10)
print(q.enQueue(5))
print(q.enQueue(15))
print(q.enQueue(25))
print(q.enQueue(53))
print(q.enQueue(55))
print(q.enQueue(51))
print(q.data)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.Front())
