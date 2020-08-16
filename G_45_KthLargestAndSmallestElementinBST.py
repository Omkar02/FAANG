# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


# from Datastruct.masterTree import readyTree, tree
# readyTree.printTree()


def kSmalestElement(node, k):
    if not node:
        return None
    if k == 0:
        return node.data
    print(k, node.data)

    l = kSmalestElement(node.lChild, k - 1)
    if l:
        return l
    r = kSmalestElement(node.rChild, k - 1)
    if r:
        return r


def getCount(node):
    if not node:
        return 0

    res = 0

    res += 1

    res += (getCount(node.lChild) + getCount(node.rChild))
    return res


k = 6
print(f'K-Smallest = {kSmalestElement(readyTree.getHead(),k-1)}')

totalNode = getCount(readyTree.getHead()) - 1
print(totalNode)
print(f'K-Largest = {kSmalestElement(readyTree.getHead(),totalNode-k-1)}')


# {
#        if(!root)
#            return 0;

#        int left = solve(root->left,k);
#        if(left)
#            return left;
#        k-=1;
#        if(k==0)
#            return root->val;
#        int right = solve(root->right,k);
#        return right;
#    }
