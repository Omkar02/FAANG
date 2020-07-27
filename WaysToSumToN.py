import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# Given a set of m distinct positive integers and a value 'N'.
# The problem is to count the total number of ways we can form 'N' by doing sum of the
# array elements. Repetitions and different arrangements are allowed.


# Examples :
# Input : arr = {1, 5, 6}, N = 7
# Output : 6

# Explanation:- The different ways are:
# 1+1+1+1+1+1+1
# 1+1+5
# 1+5+1
# 5+1+1
# 1+6
# 6+1

# Input : arr = {12, 3, 1, 9}, N = 14
# Output : 150

def waysOfSums(arr, N):
    ways = [0 for x in range(N + 1)]
    ways[0] = 1

    for i in range(1, N + 1):
        for j in range(len(arr)):
            if i >= arr[j]:

                ways[i] += ways[i - arr[j]]
    print(ways[N])


arr = [1, 5, 6]
N = 7
waysOfSums(arr, N)
