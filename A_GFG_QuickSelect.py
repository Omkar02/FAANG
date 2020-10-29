# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# def quickSelect(array, k):
#     n = len(array)
#     startIdx = 0
#     endIdx = n - 1
#     while True:
#         if startIdx > endIdx:
#             break
#         piviot = startIdx
#         left = startIdx + 1
#         right = endIdx

#         while left <= right:
#             if array[right] < array[left] and array[piviot] > array[right]:
#                 swap(array, left, right)
#             if array[left] <= array[piviot]:
#                 left += 1
#             if array[right] >= array[left]:
#                 right -= 1
#         swap(array, right, piviot)

#         if k == right:
#             return array[right]

#         elif right < k:
#             startIdx = rightIdx + 1

#         else:
#             endIdx = right - 1

def quickSelect(array, k):
    n = len(array)
    startIdx = 0
    endIdx = n - 1
    cnt = 0
    while startIdx < endIdx:
        piviot = startIdx
        left = startIdx + 1
        right = endIdx
        while left <= right:
            if array[left] > array[right] and array[piviot] > array[right]:
                swap(array, left, right)
            elif array[left] <= array[piviot]:
                left += 1
            elif array[right] >= array[piviot]:
                right -= 1
            cnt += 1
            if cnt == 100:
                return 'time excced'
        swap(array, right, piviot)
        if right == k:
            return array[k]
        elif right < k:
            startIdx = right + 1
        else:
            endIdx = right - 1
        cnt += 1
        if cnt == 100:
            return 'time excced'


def swap(a, s, o):
    a[o], a[s] = a[s], a[o]


array = [7, 10, 4, 3, 20, 15]
k = 3
print(quickSelect(array, k - 1))
