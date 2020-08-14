import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Hard')


def underscorifySubstring(string, substring):
    allOccurance = getAllOccurance(string, substring)
    mergedOccurance = getMerged(allOccurance)
    return underscorify(string, mergedOccurance)


def getAllOccurance(string, substring):
    result = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            result.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    print(result)
    return result


def getMerged(allOccurance):
    result = [allOccurance[0]]
    previous = result[0]
    for idx in range(1, len(allOccurance)):
        current = allOccurance[idx]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            result.append(current)
            previous = current
    # print(result, '0')
    return result


def underscorify(string, locations):
    locationsIdx = 0
    startIdx = 0
    isBetweenUnderScore = False
    result = []
    i = 0
    while startIdx < len(string) and locationsIdx < len(locations):
        if startIdx == locations[locationsIdx][i]:
            result.append('_')
            isBetweenUnderScore = not isBetweenUnderScore
            if not isBetweenUnderScore:
                locationsIdx += 1
            i = 0 if i == 1 else 1

        result.append(string[startIdx])
        startIdx += 1
    if locationsIdx < len(locations):
        result.append('_')

    if startIdx < len(string):
        result.append(string[startIdx:])

    return ''.join(result)


string = 'testthis is a testtest to see if testestest it works'
substring = 'test'
print(f'the req output = {underscorifySubstring(string, substring)}')
