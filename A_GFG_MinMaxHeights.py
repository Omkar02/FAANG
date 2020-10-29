# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def minMax(array, k):
    n = len(array)
    if n == 0:
        return 0
    array.sort()
    print(array, k)
    ans = arr[n - 1] - arr[0]
    print(f'ans  =  {ans}')
    small = arr[0] + k
    big = arr[n - 1] - k

    if small > big:
        small, big = big, small
    print(f'small -- > {small} | big --> {big}')
    print()
    for i in range(1, n - 1):
        sub = arr[i] - k
        add = arr[i] + k
        print(f'add = {add}  |  sub = {sub}')
        if big - sub <= add - small:
            small = sub
            print(f' |---> small {sub}')
        else:
            big = add
            print(f' |---> big {add}')
    print('============')
    return min(ans, big - small)


arr = [1, 5, 15, 10]
k = 3

arr = [1, 15, 10]
k = 6

print(minMax(arr, k))
