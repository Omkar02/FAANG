# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def isNStraightHand(hands, W):
    counts = {i: hands.count(i) for i in set(hands)}
    temp = sorted(set(hands))
    while counts:
        firstCard = min(temp)
        for i in range(firstCard, firstCard + W):
            if i not in temp:
                return False
            if counts[i] == 1:
                del counts[i]
                temp.remove(i)
            else:
                counts[i] -= 1

    return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
W = 3

hand = [1, 2, 3, 4, 5]
W = 4
print(isNStraightHand(hand, W))
