# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

cnt = [0]


def isNStraightHand(hand, W):
    cards = {x: hand.count(x) for x in set(hand)}
    theTemp = set(hand)

    while cards:
        firstCard = min(theTemp)

        for i in range(firstCard, firstCard + W):
            cnt[0] += 1

            if i not in cards:
                return False

            if cards[i] == 1:
                del cards[i]
                theTemp.remove(i)

            else:
                cards[i] -= 1

    return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
W = 5
# hand = [1, 2, 3, 4, 5]
# W = 4
hand = [x for x in range(0, 30)]

hand = [1, 2, 3, 3, 4, 4, 5, 5]
W = 3
print(isNStraightHand(hand, W))
