# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')

from Datastruct.masterLinkedList import l, v, r

l1 = [2, 4, 3]
[l.insertStart(x) for x in l1]
l2 = [5, 6, 7]
[v.insertStart(x) for x in l2]

# l.traverseList()
# v.traverseList()


def addTwoNumbers(l1, l2):
    carry = 0
    while l1 is not None or l2 is not None:
        x = l1.data if l1 else 0
        y = l2.data if l2 else 0
        total = carry + x + y
        carry = total // 10
        r.insertStart(total % 10)
        if l1:
            l1 = l1.nextNode
        if l2:
            l2 = l2.nextNode
    if carry > 0:
        r.insertStart(carry)

    r.traverseList()


addTwoNumbers(l.getHead(), v.getHead())
# while (p != null | | q != null) {
#     int x = (p != null) ? p.val: 0;
#     int y = (q != null) ? q.val: 0;
#     int sum = carry + x + y;
#     carry = sum / 10;
#     curr.next = new ListNode(sum % 10);
#     curr = curr.next;
#     if (p != null) p = p.next;
#     if (q != null) q = q.next; }
#     if (carry > 0) {
#         curr.next = new ListNode(carry)
#     }
#     return dummyHead.next
