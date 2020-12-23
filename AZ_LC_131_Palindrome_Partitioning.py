# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def palidrome_partition(s, partition, result):
    if not s:
        result.append(partition[::])
        return
    for i in range(1, len(s) + 1):
        pre, post = s[:i], s[i:]
        if is_pali(pre):
            partition.append(pre)
            palidrome_partition(post, partition, result)
            partition.pop()

    return result


def is_pali(s):
    return s == s[::-1]


s = "aab"
# Output: [["a", "a", "b"], ["aa", "b"]]
print(palidrome_partition(s, [], []))
