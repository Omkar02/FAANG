# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def filterResturants(restaurants, veganFriendly, maxPrice, maxDistance):
    restaurants = sorted(restaurants, key=lambda a: (a[1], -a[3], -a[4]), reverse=True)
    ans = []
    if veganFriendly == 0:
        return [r[0] for r in restaurants if r[3] <= maxPrice and r[4] <= maxDistance]
    return [r[0] for r in restaurants if r[2] == 1 and r[3] <= maxPrice and r[4] <= maxDistance]



#                     0    1            2           3           4
# restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10

restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10

print(filterResturants(restaurants, veganFriendly, maxPrice, maxDistance))
