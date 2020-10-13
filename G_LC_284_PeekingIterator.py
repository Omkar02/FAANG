# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


"""Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false."""


class PeekingIterator:
    def __init__(self, stack=[1, 2, 3]):
        self.stack = stack
        self.currPoint = 0
        self.size = len(self.stack)

    def next(self):
        self.currPoint += 1

    def hasNext(self):
        return self.currPoint < self.size

    def peek(self):
        if self.currPoint < self.size:
            return self.stack[self.currPoint]
        else:
            return None


p = PeekingIterator()
while p.hasNext():
    print(p.peek())
    p.next()
