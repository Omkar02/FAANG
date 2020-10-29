# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def noSpace(array):
    array.sort()
    i = 0
    n = len(array)
    print(array)
    print()
    for i in range(n):
        if array[i] > 0:
            break
    print(array[i])
    j = 0

    for _ in range(0, n // 2):
        if array[j] < 0 and array[i] > 1:
            v1, v2 = array.pop(j), array.pop(i)
            array.append(v1)
            array.append(v2)

    # array.extend(array[j:])


array = [1, 2, 3, -4, -1, 4]
noSpace(array)
print(array)
print([-4, 1, -1, 2, 3, 4])
