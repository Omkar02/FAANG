# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def simplifyPath(path):
    startsWithSlash = path[0] == '/'
    tockens = filter(isImportantToken, path.split('/'))
    stack = []
    if startsWithSlash:
        stack.append('')
    for tk in tockens:
        if tk == '..':
            if len(stack) == 0 or stack[-1] == '..':
                stack.append(tk)
            elif stack[-1] != '':
                stack.pop()

        else:
            stack.append(tk)

    return '/'.join(stack)


def isImportantToken(tocken):
    return len(tocken) > 0 and tocken != '.'


path = "/home/"
path = "/home//foo/"
path = "/a/./b/../../c/"
path = '/foo/../test/../test/../foo//bar/./baz'
path = '../../../a'
print(simplifyPath(path))
