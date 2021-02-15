# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def groupAnagram(strs):
    similar = {}
    for i in strs:
        currStr = ''.join(sorted(i))
        if currStr not in similar:
            similar[currStr] = []

        similar[currStr].append(i)
    return [value for _, value in similar.items()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagram(strs))
