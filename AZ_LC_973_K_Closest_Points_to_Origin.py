# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kColsestPoint(points, k):
    '''
        Euclidean distance.
    '''
    points.sort(key=lambda a: a[0]**2 + a[1]**2)
    return points[:k]


points = [[1, 3], [-2, 2]]
k = 1
print(kColsestPoint(points, k))
