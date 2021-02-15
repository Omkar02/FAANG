# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def findRestruant(list1, list2):

    hTwo = {}
    gotoResturant = []
    minIndexSum = float('inf')

    for idx, val in enumerate(list2):
        hTwo[val] = idx

    for idx, resturant in enumerate(list1):
        if resturant in hTwo:
            currIndexSum = idx + hTwo[resturant]
            if minIndexSum >= currIndexSum:
                minIndexSum = currIndexSum
                gotoResturant.append(resturant)

    return gotoResturant


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
# Output: ["KFC", "Burger King", "Tapioca Express", "Shogun"]
print(findRestruant(list1, list2))
