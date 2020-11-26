# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Math', Difficult='Medium')

cnt = [0]


def myPow(base, exponenet):
    cnt[0] += 1
    exponenet = abs(exponenet)
    if exponenet == 0:
        return 1
    elif exponenet % 2 == 0:
        return myPow(base * base, exponenet / 2)
    else:
        return base * myPow(base * base, (exponenet - 1) / 2)


def powFunction(base, exponenet):
    f = myPow(base, exponenet)
    return float(f) if exponenet >= 0 else 1 / f


base = float(2)
exponenet = -2
print(powFunction(base, exponenet))
print(cnt)
