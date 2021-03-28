class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.random = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
        self.curr = None
        self.dataFour = None

    def getHead(self):
        return self.head

    def getTail(self):
        return self.curr

    def insertLoop(self):
        # print(self.curr.data, self.dataFour.data)
        self.curr.nextNode = self.dataFour

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        if self.size == 4:
            # print(newNode.data, '======')
            self.dataFour = newNode

        if not self.head:
            self.head = newNode
            self.curr = self.head
        else:
            self.curr.nextNode = newNode
            self.curr = newNode

    def insertStartWithRandom(self, data, random):
        self.size = self.size + 1
        newNode = Node(data)
        newNode.random = random

        if not self.head:
            self.head = newNode
            self.curr = self.head
        else:
            self.curr.nextNode = newNode
            self.curr = newNode

    def size(self):
        return self.size

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode is not None and actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        if actualNode:
            actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:

            print(actualNode.data, end=' -> ')
            actualNode = actualNode.nextNode
        print('Null')

    def moveOn(self, node):
        actualNode = node
        while actualNode is not None:

            print(actualNode.data, end=' -> ')
            actualNode = actualNode.nextNode
        print('Null')


l = LinkedList()
r = LinkedList()
v = LinkedList()
m = LinkedList()
# print(list(range(10)))
# for i in list(range(10)):
#     l.insertStart(i)
# l.inserLoop()
# l.traverseList()
