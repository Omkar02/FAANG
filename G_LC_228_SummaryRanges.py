# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def summaryRanges(nums):
    ranges = []
    for n in nums:
        if not ranges or ranges[-1][-1] + 1 < n:
            ranges.append([])
        ranges[-1].append(n)
    return [f'{x[0]}->{x[-1]}' if x[0] != x[-1] else f'{x[0]}' for x in ranges]


nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(nums))
