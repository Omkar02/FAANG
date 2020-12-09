# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def partition(s):
    lastOcc = {c: idx for idx, c in enumerate(s)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, lastOcc[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans


s = 'ababcbacadefegdehijhklij'
print(partition(s))
