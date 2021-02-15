# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def nextLargestEle(nums):
    print('Next Large Element')
    n = len(arr)
    stack, res = [], [-1] * n
    for i in reversed(range(n)):
        while stack and nums[i] > stack[-1]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res


arr = [2, 5, 3, 8, 6]
ans = [5, 8, 8, -1, -1]

print(nextLargestEle(arr))
