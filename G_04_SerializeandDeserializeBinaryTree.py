import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Hard')


from Datastruct.masterTree import tree, BST


array = [5, 3, 1, 2, 7, 6, 8]
for i in array:
    tree.insert(i)


def serialized(root):
    seq = []
    q = [root]
    while q:
        currNode = q.pop(0)
        seq.append(currNode.data if currNode is not None else 'Null')
        if currNode is not None:
            if currNode.lChild is not None:
                q.append(currNode.lChild)
            else:
                q.append(None)
            if currNode.rChild is not None:
                q.append(currNode.rChild)
    return seq


val = serialized(tree.getHead())
print(f'seq = {val}')
# tree.printTree()
print("Deseq = ")
newTree = BST()
for j in val:
    if j != 'Null':
        newTree.insert(j)

newTree.printTree()
