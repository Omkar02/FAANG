# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def numOfRolls(dice, face, target):
    return _countTheRolls(dice, face, target, {})


def _countTheRolls(dice, face, target, cache):
    cnt[0] += 1
    curr = (dice, target)
    if curr in cache:
        return cache[curr]
    if target <= 0 or target > (face * dice):
        return 0
    if dice == 1:
        return 1

    rolls = 0
    for i in range(1, face + 1):
        rolls += _countTheRolls(dice - 1, face, target - i, cache)
    cache[curr] = rolls
    return cache[curr]


dice = 10
face = 6
target = 20
print(numOfRolls(dice, face, target))
print(cnt)
