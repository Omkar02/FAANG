# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]


# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')

from Datastruct.masterLinkedList import l, r, v, m, Node
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = Node(0)
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, (l.data, l))
        while q:
            val, node = heapq.heappop(q)
            point.next = Node(val)
            point = point.nextNode
            node = node.nextNode
            if node:
                q.put((node.data, node))
        return head.next


arrL = [1, 4, 5]
for i in arrL:
    l.insertStart(i)
arrR = [1, 3, 4]
for i in arrR:
    r.insertStart(i)
arrV = [2, 6]
for i in arrV:
    v.insertStart(i)


lists = [l.getHead(), r.getHead(), v.getHead()]

Klist = Solution()
Klist.mergeKLists(lists)
