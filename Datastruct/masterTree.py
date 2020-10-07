class bNode:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class BST():
    def __init__(self):
        self.root = None

    def getHead(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = bNode(data)
        else:
            self._insertInto(self.root, data)

    def _insertInto(self, node, data):
        if data < node.data:
            if not node.lChild:
                node.lChild = bNode(data)
            else:
                self._insertInto(node.lChild, data)
        else:
            if not node.rChild:
                node.rChild = bNode(data)
            else:
                self._insertInto(node.rChild, data)

    def Serach(self, data):
        actNode = self.root
        while actNode:
            if data < actNode.data:
                if actNode.data == data:
                    print('Found!')
                    return
                else:
                    actNode = actNode.lChild
            else:
                if actNode.data == data:
                    print('Found!')
                    return
                else:
                    actNode = actNode.rChild
        print('Nee!')

    def printTree(self):
        try:
            lines, _, _, _ = self._display_aux(self.root)
            for line in lines:
                print(line)

        except Exception as e:
            pass

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        try:
            if node.rChild is None and node.lChild is None:
                line = '%s' % node.data
                width = len(line)
                height = 1
                middle = int(width // 2)
                return [line], width, height, middle

            # Only left child.
            if node.rChild is None:
                lines, n, p, x = self._display_aux(node.lChild)
                s = '%s' % node.data
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if node.lChild is None:
                lines, n, p, x = self._display_aux(node.rChild)
                s = '%s' % node.data
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = self._display_aux(node.lChild)
            right, m, q, y = self._display_aux(node.rChild)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
        except:
            pass


tree = BST()


readyTree = BST()
array = [6, 2, 1, 3, 5, 8, 7, 9, 10]
array = [7, 2, 1, 3, 5, 8, 9, 10]
for i in array:
    readyTree.insert(i)


class aNode():
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

        self.height = 0


val = []


class AVL():
    def __init__(self):
        self.root = None

    def _calHeight(self, node):
        if not node:
            return -1
        return node.height

    def _calBalance(self, node):
        if not node:
            return 0
        return self._calHeight(node.lChild) - self._calHeight(node.rChild)

    def _rotateRight(self, node):
        print(f'Rotating node {node.data} to right!')
        templeftChild = node.lChild
        t = templeftChild.rChild

        templeftChild.rChild = node
        node.lChild = t

        node.height = max(self._calHeight(node.lChild), self._calHeight(node.rChild)) + 1
        templeftChild.height = max(self._calHeight(templeftChild.lChild), self._calHeight(templeftChild.rChild)) + 1

        return templeftChild

    def _rotateLeft(self, node):
        print(f'Rotating node {node.data} to left!')
        tempRightChild = node.rChild
        t = tempRightChild.lChild

        tempRightChild.lChild = node
        node.rChild = t

        node.height = max(self._calHeight(node.lChild), self._calHeight(node.rChild)) + 1
        tempRightChild.height = max(self._calHeight(tempRightChild.lChild), self._calHeight(tempRightChild.rChild)) + 1

        return tempRightChild

    def iAvl(self, data):
        self.root = self._insertA(data, self.root)

    def _insertA(self, data, node):
        if not node:
            return aNode(data)
        if data < node.data:
            node.lChild = self._insertA(data, node.lChild)
        if data > node.data:
            node.rChild = self._insertA(data, node.rChild)

        node.height = max(self._calHeight(node.lChild), self._calHeight(node.rChild)) + 1
        return self._checkViolation(data, node)
        # return node

    def _checkViolation(self, data, node):
        balance = self._calBalance(node)

        # case1: it is a left-left heavy situation
        if balance > 1 and data < node.lChild.data:
            print('left-left heavy situation | Rotating right..')
            return self._rotateRight(node)

        # case2: it is a right right heavy situation
        if balance < -1 and data > node.rChild.data:
            print('right-right heavy situation | Rotating left')
            return self._rotateLeft(node)

        # case3: it is a left right heavy situation
        if balance > 1 and data > node.lChild.data:
            print('left-right heavy situation | Rotating left-right')
            node.lChild = self._rotateLeft(node.lChild)
            return self._rotateRight(node)

        # case4: it is a right left heavy situation
        if balance < -1 and data < node.rChild.data:
            print('right left heavy situation | Rotating right-left')
            node.rChild = self._rotateRight(node.rChild)
            return self._rotateLeft(node)

        return node

    def _removeViolation(self, node):
        if not node:
            return node

        node.height = max(self._calHeight(node.lChild), self._calHeight(node.rChild)) + 1
        balance = self._calBalance(node)

        # case1: it is a left-left heavy situation
        if balance > 1 and self._calBalance(node.lChild) >= 0:
            print('left-left heavy situation | Rotating right..')
            return self._rotateRight(node)

        # case2: it is a right right heavy situation
        if balance < -1 and self._calBalance(node.rChild) <= 0:
            print('right-right heavy situation | Rotating left')
            return self._rotateLeft(node)

        # case3: it is a left right heavy situation
        if balance > 1 and self._calBalance(node.lChild) < 0:
            print('left-right heavy situation | Rotating left-right')
            node.lChild = self._rotateLeft(node.lChild)
            return self._rotateRight(node)

        # case4: it is a right left heavy situation
        if balance < -1 and self._calBalance(node.rChild) > 0:
            print('right left heavy situation | Rotating right-left')
            node.rChild = self._rotateRight(node.rChild)
            return self._rotateLeft(node)

        return node

    def remove(self, data):
        if self.root:
            self.root = self._removeNode(data, self.root)

    def _removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.lChild = self._removeNode(data, node.lChild)

        elif data > node.data:
            node.rChild = self._removeNode(data, node.rChild)

        else:
            if not node.lChild and not node.rChild:
                print('Deleting Leaf node!')
                del node
                return None

            if not node.lChild:
                print('Deleting right child!')
                tempnode = node.rChild
                del node
                return tempnode

            if not node.rChild:
                print('Deleting left child!')
                tempnode = node.lChild
                del node
                return tempnode

            print('Deleting node with Two  child!')
            print(node.lChild.data)
            tempnode = self._getPredsessor(node.lChild)
            # print(tempnode,'============')
            node.data = tempnode.data
            node.lChild = self._removeNode(tempnode.data, node.lChild)

        # if not node:

        return self._removeViolation(node)  # MAGIC
        # return node

    def _getPredsessor(self, node):
        if node.rChild:
            return self._getPredsessor(node.rChild)
        return node

    def traverse(self):
        if self.root:
            self._traInter(self.root)

    def _traInter(self, node):
        if node.lChild:
            self._traInter(node.lChild)

        # print(node.data)
        val.append(node.data)

        if node.rChild:
            self._traInter(node.rChild)

    def printTree(self):
        try:
            lines, _, _, _ = self._display_aux(self.root)
            for line in lines:
                print(line)

        except Exception as e:
            pass

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.rChild is None and node.lChild is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = int(width // 2)
            return [line], width, height, middle

        # Only left child.
        if node.rChild is None:
            lines, n, p, x = self._display_aux(node.lChild)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.lChild is None:
            lines, n, p, x = self._display_aux(node.rChild)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.lChild)
        right, m, q, y = self._display_aux(node.rChild)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


avl = AVL()


# array = [21, 26, 30, 9, 4, 14, 28]
# for i in array:
#     avl.iAvl(i)


# avl.printTree()
