import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Hard')


from Datastruct.masterGraphs import g


def commonAncestor(root, nodeOne, nodeTwo):
    depthOne = getDepth(nodeOne, root)
    depthTwo = getDepth(nodeTwo, root)
    diff = abs(depthOne - depthTwo)
    if depthOne > depthTwo:
        return ancenstorTreeTraverse(nodeOne, nodeTwo, diff)
    else:
        return ancenstorTreeTraverse(nodeTwo, nodeOne, diff)


def getDepth(node, root):
    depth = 0
    while node.data != root.data:
        depth += 1
        node = node.ancenstor
    return depth


def ancenstorTreeTraverse(lower, higher, diff):
    while diff != 0:
        lower = lower.ancenstor
        diff -= 1

    while lower.data != higher.data:
        lower = lower.ancenstor
        higher = higher.ancenstor
    return lower.data


g.setHead('A')
# test

B = g.insert('B')
C = g.insert('C')
D = g.insert('D')
E = g.insert('E')
F = g.insert('F')
G = g.insert('G')
H = g.insert('H')
I = g.insert('I')
J = g.insert('J')
K = g.insert('K')
L = g.insert('L')
M = g.insert('M')
N = g.insert('N')
O = g.insert('O')
P = g.insert('P')
Q = g.insert('Q')
R = g.insert('R')
T = g.insert('T')
U = g.insert('U')
V = g.insert('V')
W = g.insert('W')
X = g.insert('X')
Y = g.insert('Y')
Z = g.insert('Z')


g.getHead().addNodes([B, C, D, E, F])

B.addNodes([G, H, I])
B.ancenstor = g.getHead()

C.addNodes([J])
C.ancenstor = g.getHead()

D.addNodes([K, L])
D.ancenstor = g.getHead()

E.ancenstor = g.getHead()

F.addNodes([M, N])
F.ancenstor = g.getHead()

G.ancenstor = B

H.ancenstor = B
H.addNodes([O, P, Q, R])

I.ancenstor = B

J.ancenstor = C

K.ancenstor = D

L.ancenstor = D

M.ancenstor = F

N.ancenstor = F

O.ancenstor = H

P.ancenstor = H
P.addNodes([T, U])

Q.ancenstor = H

R.ancenstor = H
R.addNodes([V])

T.ancenstor = P

U.ancenstor = P

V.ancenstor = R
V.addNodes([W, X, Y])

W.ancenstor = V

X.ancenstor = V
X.addNodes([Z])

Y.ancenstor = V

Z.ancenstor = X

# g.printGraphs()
topAncestor = g.getHead()
# print(topAncestor.data)
val = commonAncestor(topAncestor, N, T)
print(f'|--> The Smallest Common Ancenstor = |{val}|')
print('=' * 47)
