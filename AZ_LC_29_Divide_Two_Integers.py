# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Math', Difficult='Medium')


def divide(dividend, divisor):
    flag = 0
    if dividend < 0:
        if divisor > 0:
            flag = 1
    elif divisor < 0:
        flag = 1
    if(dividend == -2147483648 and divisor == -1):
        return 2147483647

    res = 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        dividend -= divisor
        res += 1

    if flag:
        return - 1 * res

    return res

'''----------------------------------------------------------------------'''
import math


def divide(dividend, divisor):
    flag = 0
    if dividend < 0:
        if divisor > 0:
            flag = 1
    elif divisor < 0:
        flag = 1
    if(dividend == -2147483648 and divisor == -1):
        return 2147483647

    ans = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
    ans = int(ans)
    return ans if not flag else -1 * ans


dividend = 10
divisor = 3

dividend = 7
divisor = -3

print(divide(dividend, divisor))
