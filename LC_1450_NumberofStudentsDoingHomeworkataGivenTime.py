import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.


def busyStudent(startTime, endTime, queryTime):
    cnt = 0
    for x in zip(startTime, endTime):
        # print(x)
        if x[0] <= queryTime and x[1] >= queryTime:
            cnt += 1
    return cnt


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4


print(f'Number Of busy stu = {busyStudent(startTime,endTime,queryTime)}')
