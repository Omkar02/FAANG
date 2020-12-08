# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Easy')


def balancedStringSplit(s):
    pair = count = 0
    for i in s:
        if i == 'R':
            pair += 1
        else:
            pair -= 1

        if not pair:
            count += 1
    return count


s = 'RLRRLLRLRL'
print(balancedStringSplit(s))
