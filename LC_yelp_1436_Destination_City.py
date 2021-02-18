# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def getDestinantionCity(paths):
    routes = {val: False for x in paths for val in x}
    for scr, dst in paths:
        if scr in routes:
            routes[scr] = True
    # print(routes)
    for location in routes:
        if not routes[location]:
            return location
    return -1


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths = [["B", "C"], ["D", "B"], ["C", "A"]]
print(getDestinantionCity(paths))
