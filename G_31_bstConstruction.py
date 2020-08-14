import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


class bstNode():
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class tree():
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, data):
        newNode = bstNode(data)
        if self.root is None:
            self.root = newNode
        else:
            self._insertInto(data, self.root)

    def _insertInto(self, data, node):
        if data < node.data:
            if not node.lChild:
                node.lChild = bstNode(data)
            else:
                self._insertInto(data, node.lChild)
        else:
            if not node.rChild:
                node.rChild = bstNode(data)
            else:
                self._insertInto(data, node.rChild)

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


tr = tree()

import random

arr = [i for i in range(10)]
random.shuffle(arr)
print(arr)
for i in arr:
    tr.insert(i)

tr.printTree()
