# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findAnagram(s, p):
    p = ''.join(sorted(p))
    n = len(s)
    ans = []
    temp = ''
    start = 0
    for i in range(n):
        temp += s[i]
        if len(temp) == len(p):
            print(temp)
            currWord = ''.join(sorted(temp))
            if currWord == p:
                ans.append(start)
                
        if len(temp) == 3:
            temp = ''
            start = i
    return ans


s = "cbaebabacd"
p = "abc"
print(findAnagram(s, p))
