import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def fib(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n - 1, b, a + b)


n = 9
print(fib(n))
