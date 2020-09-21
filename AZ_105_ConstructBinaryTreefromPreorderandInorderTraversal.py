# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import tree, bNode
"""
preorder = root --> left --> right
inorder =  left --> root --> right
postorder = left --> right --> root
"""


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

from collections import defaultdict


class Solution:
    def buildTree(self, preorder, inorder):
        idxmap = defaultdict(int)

        for i, n in enumerate(inorder):
            idxmap[n] = i

        return self.helper(preorder[::-1], inorder, 0, len(inorder), idxmap)

    def helper(self, preorder, inorder, leftPointer, rightPointer, idxmap):
        if leftPointer < rightPointer:
            num = preorder.pop()
            root = bNode(num)
            idx = idxmap.get(num)

            root.lChild = self.helper(preorder, inorder, leftPointer, idx, idxmap)
            root.rChild = self.helper(preorder, inorder, idx + 1, rightPointer, idxmap)

            # if root:
            #     print(f'R = {root.data}')
            # if root.lChild:
            #     print(f'\t\tL = {root.lChild.data}')
            # if root.rChild:
            #     print(f'\tR = {root.rChild.data}')
            # print()
            return root


s = Solution()
print(s.buildTree(preorder, inorder))
