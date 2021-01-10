# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def videoStitching(clips, T):
    clips.sort(key=lambda x: (x[0], x[1]))
    right = 0
    idx = 0
    count = 0
    print(clips)
    while idx < len(clips):
        if clips[idx][0] > right:
            return -1

        farReach = right
        while idx < len(clips) and clips[idx][0] <= right:
            farReach = max(farReach, clips[idx][1])
            idx += 1

        right = farReach
        count += 1
        print(farReach)
        if farReach >= T:
            return count

    return -1


clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
T = 10
print(videoStitching(clips, T))
