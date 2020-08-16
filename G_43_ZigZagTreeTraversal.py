# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def zigZagTaverse(head):
    if not head:
        return [-1]

    isLeftToRight = True
    currentLevel = [head]
    nextLevel = []

    result = []

    while currentLevel:
        currVal = currentLevel.pop()
        result.append(currVal.data)

        if isLeftToRight:
            if currVal.lChild:
                nextLevel.append(currVal.lChild)
            if currVal.rChild:
                nextLevel.append(currVal.rChild)
        else:
            if currVal.rChild:
                nextLevel.append(currVal.rChild)
            if currVal.lChild:
                nextLevel.append(currVal.lChild)

        if len(currentLevel) == 0:
            isLeftToRight = not isLeftToRight
            nextLevel, currentLevel = currentLevel, nextLevel

    return result


print(f'Zig Zag Order = {zigZagTaverse(readyTree.getHead())}')
