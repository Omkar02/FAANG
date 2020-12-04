# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def rotateString(A, B):
    print(A + A)
    return len(A) == len(B) and B in A + A


A = 'abcde'
B = 'cdeab'

A = 'abcde'
B = 'abced'
print(rotateString(A, B))
