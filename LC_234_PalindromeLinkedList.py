# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l


def isPalindrome(lLint):
    head = lLint.getHead()
    tail = lLint.getTail()
    size = lLint.size
    mid = (size / 2) if size % 2 == 0 else (size + 1) / 2

    reverseTheOtherHalf(head, mid, size)

    return isPaliHelper(head, tail, mid)


def reverseTheOtherHalf(node, mid, size):
    Idx = 0
    temp = None
    temp2 = None
    while Idx < size:
        if Idx >= mid:
            temp2 = node.nextNode
            node.nextNode = temp

            temp = node
            node = temp2

        else:
            temp = node
            node = node.nextNode
        Idx += 1


def isPaliHelper(head, tail, mid):
    print('Checking...')
    idx = 0
    while idx < mid:
        print(f'\t{head.data} | {tail.data}')
        if tail.data != head.data:
            return False

        idx += 1

        if idx > mid:
            return 'Ne!'

        tail = tail.nextNode
        head = head.nextNode

    return True


arr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]

# arr = [1, 2, 3, 2, 1]
[l.insertStart(x) for x in arr]
print('Original = ', end=' ')
l.traverseList()


print(f'Palindrome =  {isPalindrome(l)}')
