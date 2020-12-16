# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def nextGreaterEle(nums):
    n = len(nums)
    if not n:
        return []
    res = [-1] * n
    stack = []
    ''' Run it twice. After first iteration
        the stack has the increasing order of elements from starting
        so in second iteration you will get the next greater from stack
        which was on the left side of that node '''
    for _ in range(2):
        for i in reversed(range(n)):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
    return res


print(nextGreaterEle(nums))
