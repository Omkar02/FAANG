# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='S', filename=fileName, Tag='Array', Difficult='Medium')


def nextGreaterEle(nums):
    stack = [nums[0]]
    ele = 0
    nxt = 0
    n = len(nums)
    for i in range(1, n):
        nxt = nums[i]
        if stack:
            ele = stack.pop()
            while ele < nxt:
                print(f'{ele} -- > {nxt}')
                if not stack:
                    break
                ele = stack.pop()
            if ele > nxt:
                stack.append(ele)
        stack.append(nxt)
    while len(stack) != 0:
        ele = stack.pop()
        nxt = -1
        print(f'{ele} -- > {nxt}')


nums = [4, 3, 2, 1, 5, 2, 25]
nextGreaterEle(nums)
