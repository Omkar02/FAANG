# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def longWithabsdiff(array, limit):
    minDeQ = array[0]
    maxDeQ = array[0]
    maxLength = 1

    start = 0
    end = 1
    n = len(array)
    while start <= end and end < n:
        minDeQ = min(minDeQ, array[end])
        maxDeQ = max(maxDeQ, array[end])

        if (maxDeQ - minDeQ) <= limit:
            maxLength = max(maxLength, end - start + 1)

        else:
            if array[start] == maxDeQ:
                maxDeQ = max(array[start + 1:end + 1])

            if array[end] == minDeQ:
                minDeQ = min(array[start + 1:end + 1])
            start += 1
        end += 1
    return maxLength


array = [8, 2, 4, 7]
limit = 4
print(longWithabsdiff(array, limit))
