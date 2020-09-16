# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


dictionary = ["abb", "abc", "xyz", "xyy"]
pattern = "foo"
dictionary = ["abb", "xyz", "aab", "kmm"]
pattern = "stt"
# Output: [xyy abb]

cnt = [0]


def AllWords(pattern, dictionary):
    ans = []
    for word in dictionary:
        helperPat(pattern, word, ans)
        print(word)

    return ans


def helperPat(pattern, word, ans):
    if len(pattern) != len(word):
        return
    n = len(pattern)
    patMap = {x: -1 for x in pattern}
    # print(f'\t{patMap}')
    for i in range(n):
        cnt[0] += 1
        if patMap[pattern[i]] == -1 or patMap[pattern[i]] == word[i]:
            patMap[pattern[i]] = word[i]
        else:
            return
    print('--- >', end=' ')
    ans.append(word)


print(AllWords(pattern, dictionary))
print(cnt)
