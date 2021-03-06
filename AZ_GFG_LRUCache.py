# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Hard')

"""
class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextNode = None
        self.prevNode = None

    def clearBuindings(self):
        if self.prevNode:
            self.prevNode.nextNode = self.nextNode

        if self.nextNode:
            self.nextNode.prevNode = self.prevNode

        self.nextNode = None
        self.prevNode = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeatTo(self, node):
        if self.head == node:
            return

        elif not self.head:
            self.head = node
            self.tail = node

        elif self.head == self.tail:
            self.tail.prevNode = node
            self.head = node
            self.head.nextNode = self.tail

        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prevNode = node
            node.nextNode = self.head
            self.head = node

    def removeTail(self):
        if not self.tail:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prevNode
        self.tail.nextNode = None


class LRUCache:
    def __init__(self, maxsize=1):
        self.cache = {}
        self.maxsize = maxsize
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def insertValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxsize:
                self.evecitLeastRecent()
            else:
                self.currentSize += 1

            self.cache[key] = node(key, value)

        else:
            self.replaceKey(key, value)

        self.updateMostRecent(self.cache[key])

    def evecitLeastRecent(self):
        print(f'\tevicted --> {self.listOfMostRecent.tail.key}')
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeatTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception('NeNe!')

        self.cache[key].value = value

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None

        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecent(self):
        return self.listOfMostRecent.head.key


l = LRUCache(1)
arr = [(1, 'a'), (1, 'g'), (4, 'd'), (5, 'e'), (2, 'b'), (2, 'c')]

for i in arr:
    l.insertValuePair(i[0], i[1])
    print(l.getMostRecent())

print(l.cache)
"""


class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prv = None

    def removeBingings(self):
        if self.prv:
            self.prv.nxt = self.nxt
        if self.nxt:
            self.nxt.prv = self.prv

        self.nxt = None
        self.prv = None


class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return

        elif not self.head:
            self.head = node
            self.tail = node

        elif self.head == self.tail:
            self.tail.prv = node
            self.head = node
            self.head.nxt = self.tail

        else:
            if self.tail == node:
                self.removeTail()
            node.removeBingings()
            self.head.prv = node
            node.nxt = self.head
            self.head = node

    def removeTail(self):
        if not self.tail:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prv
        self.tail.nxt = None


class LRU_Cache:
    def __init__(self, maxsize=1):
        self.cache = {}
        self.maxsize = maxsize
        self.currentSize = 0
        self.listOfMostRecent = doubleLinkedList()

    def insertValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxsize:
                self.evecitLeastRecent()
            else:
                self.currentSize += 1

            self.cache[key] = node(key, value)
        else:
            self.cache[key].value = value

        self.updateMostRecent(self.cache[key])

    def evecitLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None

        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecent(self):
        return self.listOfMostRecent.head.key


l = LRU_Cache(1)
arr = [(1, 'a'), (1, 'g'), (4, 'd'), (5, 'e'), (2, 'b'), (2, 'c')]

for i in arr:
    l.insertValuePair(i[0], i[1])
    print(l.getMostRecent())

print(l.cache)
