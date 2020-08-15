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
for i in array:
    readyTree.insert(i)


class Anode():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

        self.height = 0


class AVL():
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def _calHeight(self, node):
        if not node:
            return -1
        return node.height

    def _calBalance(self, node):
        if not node:
            return 0
        return self._calHeight(node.left) - self._calHeight(node.right)

    def _rotateRight(self, node):
        # print(f'Rotating {node.data} to right!')
        templeftChild = node.left
        t = templeftChild.right

        templeftChild.right = node
        node.left = t

        node.height = max(self._calHeight(node.left), self._calHeight(node.right)) + 1
        templeftChild.height = max(self._calHeight(templeftChild.left), self._calHeight(templeftChild.right)) + 1

        return templeftChild

    def _rotateLeft(self, node):
        # print(f'Rotating node {node.data} to left!')
        tempRightChild = node.right
        t = tempRightChild.left

        tempRightChild.left = node
        node.right = t

        node.height = max(self._calHeight(node.left), self._calHeight(node.right)) + 1
        tempRightChild.height = max(self._calHeight(tempRightChild.left), self._calHeight(tempRightChild.right)) + 1

        return tempRightChild

    def iAvl(self, data):
        self.root = self._insertAvl(data, self.root)

    def _insertAvl(self, data, node):
        if not node:
            return Anode(data)

        if data < node.data:
            node.left = self._insertAvl(data, node.left)

        if data > node.data:
            node.right = self._insertAvl(data, node.right)

        node.height = max(self._calHeight(node.left), self._calHeight(node.right)) + 1

        # return node
        return self._insVoilation(data, node)

    # return self._calHeight(node.left) - self._calHeight(node.right)
    def _insVoilation(self, data, node):
        balance = self._calBalance(node)
        # print(f'{balance}------------------{data}')
        # case LL
        if balance > 1 and node.left.data > data:
            # print('LL!')
            return self._rotateRight(node)
        # case LR
        if balance > 1 and node.left.data < data:
            # print('LR')
            node.left = self._rotateLeft(node)
            return self._rotateRight(node)
        # case RR
        if balance < -1 and node.right.data < data:
            # print('RR')
            return self._rotateLeft(node)
        # case RL
        if balance < -1 and node.right.data > data:
            # print('RL')
            node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def trav(self):
        self._traverceAVL(self.root)

    def printTree(self):
        try:
            lines, _, _, _ = self._display_aux(self.root)
            for line in lines:
                print(line)

        except Exception as e:
            pass

    def _traverceAVL(self, node):
        if node.left:
            self._traverceAVL(node.left)
        print(node.data, '-------')

        if node.right:
            self._traverceAVL(node.right)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = int(width // 2)
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
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

    def finder(self, data):
        val = self._findData(data, self.root)
        print(f'Found :  {val}')

    def _findData(self, data, node):

        if not node:
            return None
        else:
            print(f'Visited --> {node.data}')

        if node.data == data:
            return node.data

        if data < node.data:
            return self._findData(data, node.left)

        elif data > node.data:
            return self._findData(data, node.right)


avl = AVL()
