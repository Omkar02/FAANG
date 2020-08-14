import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


class node():
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        self.curr = None

    def getHead(self):
        return self.head

    def insert(self, data):
        self.size += 1
        newNode = node(data)

        if not self.head:
            self.head = newNode
            self.curr = newNode

        else:
            self.curr.nextNode = newNode
            self.curr = newNode

    def printList(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end=' --> ')
            currNode = currNode.nextNode
        print('Null')

    def remove(self, val):
        currNode = self.head
        if val == self.head.data:
            self.head = currNode.nextNode
            return

        while currNode.nextNode.data != val:
            currNode = currNode.nextNode
        currNode.nextNode = currNode.nextNode.nextNode


l = LinkedList()
arr = [1, 2, 3, 4, 5]
for k in arr:
    l.insert(k)
l.remove(4)
l.printList()
