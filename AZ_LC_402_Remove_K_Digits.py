# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def removeKdigits(num, k):
    stack = []
    for i in range(len(num)):

        curr = num[i]
        while stack and k and num[i] < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(curr)
        print(stack)

    if k:
        del stack[-k:]
    res = ''.join(stack).lstrip('0')
    return res if res else '0'


num = "1432219"
k = 3

print(removeKdigits(num, k))
