# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def nextGreaterElement(arr1, arr2):
    stack, hashmap = [], {}
    for num in arr2:
        while stack and stack[-1] < num:
            hashmap[stack.pop()] = num
        stack.append(num)

    return [hashmap.get(num, -1) for num in arr1]


arr1, arr2 = [4, 1, 2], [1, 3, 4, 2]
out = [-1, 3, -1]

print(nextGreaterElement(arr1, arr2))
