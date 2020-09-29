# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def totalFruit(tree):
    basket = {}
    ans = preFruitIdx = 0
    for endIdx, fruit in enumerate(tree):
        if fruit not in basket:
            basket[fruit] = 0
        basket[fruit] += 1
        while len(basket) >= 3:

            basket[tree[preFruitIdx]] -= 1
            if basket[tree[preFruitIdx]] == 0:
                del basket[tree[preFruitIdx]]

            preFruitIdx += 1

        ans = max(ans, endIdx - preFruitIdx + 1)

    return ans


tree = [1, 2, 1]
tree = [1, 2, 3, 2, 2]
tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(tree))
