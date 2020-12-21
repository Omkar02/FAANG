# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def shipWithinDays(weights, D):
    n = len(weights)
    lo, hi = max(weights), sum(weights)
    while lo <= hi:
        capacity = (hi + lo) // 2
        if days_required(capacity, weights, n) < D:
            hi = capacity - 1
        else:
            lo = capacity + 1
    return lo


def days_required(capacity, weights, n):
    running_sum = 0
    days = 0
    for i in range(n):
        running_sum += weights[i]
        if running_sum > capacity:
            running_sum = weights[i]
            days += 1
    return days


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
print(shipWithinDays(weights, D))
