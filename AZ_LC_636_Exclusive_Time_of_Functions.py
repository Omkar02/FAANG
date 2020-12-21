# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def getExclusiveTime(n, logs):

    logs = [mapLogs(log.split(':')) for log in logs]         # convert [string] to [(,,)]
    ans, s = [0] * n, []                                    # initialize answer and stack
    for (i, status, timestamp) in logs:                     # for each record
        if status == 'start':                               # if it's start
            if s:
                ans[s[-1][0]] += timestamp - s[-1][1]     # if s is not empty, update time spent on previous id (s[-1][0])
            s.append([i, timestamp])                        # then add to top of stack
        else:                                               # if it's end
            ans[i] += timestamp - s.pop()[1] + 1            # update time spend on `i`
            if s:
                s[-1][1] = timestamp + 1                    # if s is not empty, udpate start time of previous id;
    return ans


def mapLogs(log):
    return (int(log[0]), log[1], int(log[2]))  # to covert id and time to integer


n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
# Output: [3, 4]
print(getExclusiveTime(n, logs))
