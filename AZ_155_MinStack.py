# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, data):
        if not self.stack:
            self.stack.append(data)
            self.minStack.append(data)
            return
        self.stack.append(data)
        minVal = min(self.minStack[-1], data)
        self.minStack.append(minVal)

    def pop(self):
        if not self.stack:
            return None
        self.minStack.pop(-1)
        return self.stack.pop(-1)

    def top(self):
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


arr = [6, 5, 4, 3, 2, 1]
S = minStack()

# for i in arr:
#     S.push(i)
#     print(S.stack, '|', S.minStack)
# print()
# for i in arr:
#     S.pop()
#     print(S.stack, '|', S.minStack)
