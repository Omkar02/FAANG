import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def nodeWithK(node, k, res):

    if (node == None):
        return (0, res)

    # if node is leaf
    if (node.lChild == None and
            node.rChild == None):
        return (1, res)

    # total leaves in subtree rooted with this
    # node
    total = nodeWithK(node.lChild, k, res)[0] + nodeWithK(node.rChild, k, res)[0]

    # Prthis node if total is k
    if (k == total):
        res.append(node.data)
    return total, res


k = 2
_, nodes = nodeWithK(readyTree.getHead(), k, [])
print(f'Nodes with {k} leaves = {nodes if len(nodes) else None}')
