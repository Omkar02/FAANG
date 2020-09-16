# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def dailyTemperatures(T):
    n = len(T)
    daysOfWait = [-1] * n
    stack = []

    for i in range(n):
        while stack and T[stack[-1]] < T[i]:
            daysOfWait[stack[-1]] = i - stack[-1]
            stack.pop()

        stack.append(i)

    return daysOfWait


arr = [73, 74, 75, 71, 69, 72, 76, 73]

print(dailyTemperatures(arr))
