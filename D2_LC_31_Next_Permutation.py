# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def nxtPermution(num):
    i = len(num) - 2
    # "b = find the num[i]>num[i+1] | reverse pass"
    while i >= 0 and num[i + 1] <= num[i]:
        i -= 1
    # "a = find the num[i]<num[i+1] | reverse pass"
    print(i)
    if i >= 0:
        j = i
        while j >= 0 and num[j] <= num[i]:
            j -= 1
        # "swap a with b"
        print(j)
        swap(num, i, j)
    # "reverse all after the 'a index' "
    reverse(num, i + 1)

    return num


def reverse(num, start):
    end = len(num) - 1
    while start < end:
        swap(num, start, end)
        start += 1
        end -= 1


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


num = [1, 2, 3, 4]
print(nxtPermution(num))
