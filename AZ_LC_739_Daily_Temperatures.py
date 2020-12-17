# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def nxtHotestTemp(temp):
    n = len(temp)
    stack = []
    ans = [0 for _ in temp]
    for i in reversed(range(n)):
        while stack and temp[i] >= temp[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans


temp = [73, 74, 75, 71, 69, 72, 76, 73]
output = [1, 1, 4, 2, 1, 1, 0, 0]
print(nxtHotestTemp(temp) == output)
