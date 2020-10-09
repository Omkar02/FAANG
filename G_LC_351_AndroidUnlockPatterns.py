# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total 
number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
Rules for a valid pattern:
Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other 
keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
"""


"""https://www.geeksforgeeks.org/number-of-ways-to-make-mobile-lock-pattern/"""


# |1 | 2 | 3|
# |4 | 5 | 6|
# |7 | 8 | 9|

class android:
    def __init__(self):
        self.count = 0
        self.skip = {(1, 3): 2,
                     (1, 7): 4,
                     (1, 9): 5,
                     (2, 8): 5,
                     (3, 7): 5,
                     (3, 9): 6,
                     (4, 6): 5,
                     (7, 9): 8}

    def androidUnlockPattern(self, m, n):

        # for curr in range(1, 10):
        #     self.backtrack(curr, set([curr]))
        self.backtrack(1, set([1]))
        self.backtrack(2, set([2]))
        self.count *= 4
        self.backtrack(5, set([5]))
        return self.count

    def backtrack(self, curr, visited):
        # print(visited, curr)
        if len(visited) >= m:
            self.count += 1
        if len(visited) == n:
            return

        for nxt in range(1, 10):
            if nxt in visited:
                continue

            edge = (min(curr, nxt), max(curr, nxt))
            # print(edge)
            if edge not in self.skip or self.skip[edge] in visited:
                visited.add(nxt)
                self.backtrack(nxt, visited)
                visited.remove(nxt)


m = 1
n = 1
a = android()
print(a.androidUnlockPattern(m, n))
