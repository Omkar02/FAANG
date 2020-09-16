# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def longestPalindrome(s):
    currLongest = [0, 1]
    n = len(s)
    for i in range(1, n):
        odd = getPali(s, i - 1, i + 1)
        even = getPali(s, i - 1, i)

        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currLongest = max(currLongest, longest, key=lambda x: x[1] - x[0])
    return currLongest, s[currLongest[0]:currLongest[1]]


def getPali(string, l, r):
    while l > 0 and r < len(s):
        if s[l] != s[r]:
            break
        l -= 1
        r += 1
    return [l + 1, r]


s = "babad"
print(longestPalindrome(s))
