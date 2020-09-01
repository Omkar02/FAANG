# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def numTeams(rating):

    count, n = 0, len(rating)
    for j in range(1, n - 1):
        lt = sum(rating[i] < rating[j] for i in range(j))
        gt = sum(rating[j] < rating[k] for k in range(j + 1, n))
        count += lt * gt + (j - lt) * (n - j - gt - 1)
    return count


ratings = [2, 5, 3, 4, 1]
ratings = [2, 1, 3]
print(f'THe numTeams = {numTeams(ratings)}')
