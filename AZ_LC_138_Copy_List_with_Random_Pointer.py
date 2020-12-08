# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')
from Datastruct.masterLinkedList import l


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.random = None


def copyRandomList(head):
    if head is None:
        return None
    # first pass to make the copy node
    node_to_clone = dict()
    node = head
    clone_head = Node(head.data)
    node_to_clone[head] = clone_head
    clone_node = clone_head
    while node.nextNode:
        clone_node.nextNode = Node(node.nextNode)
        node = node.nextNode
        clone_node = clone_node.nextNode
        node_to_clone[node] = clone_node
    # second pass to make the wiring
    node = head
    while node:
        if node.random:
            clone_node = node_to_clone[node]
            clone_node.random = node_to_clone[node.random]
        node = node.nextNode
    return clone_head


ogList = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

for o in ogList:
    l.insertStartWithRandom(o[0], o[1])
# l.traverseList()
copyRandomList(l.getHead())
