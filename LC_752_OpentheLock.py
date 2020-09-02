# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


# start = list('00000')
# cnt = 0
# idx = 0
# n = len(start)
# while cnt < 1000 and idx < n:
#     print(''.join(start), end=' ')
#     start[idx] = str(int(start[idx]) + 1)
#     # start = f'{start[0:idx]}{str(currNum)}{start[idx:n-1]}'
#     if int(start[idx]) == 9:
#         print()
#         idx += 1
#     cnt += 1

cntq = [0]


def openLock(deadends, target):
    q = [(0, '0000')]
    deadends = set(deadends)
    start = ['0000']
    visited = set(start)

    if target == '0000':
        return -1

    while q:
        step, lock = q.pop(0)

        for i in range(4):
            cntq[0] += 1
            prv = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i + 1:]
            nxt = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:]

            if prv == target or nxt == target:
                return step + 1

            if prv not in deadends:
                q.append((step + 1, prv))
                deadends.add(prv)

            if nxt not in deadends:
                q.append((step + 1, nxt))
                deadends.add(nxt)
    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(openLock(deadends, target))
print(cntq)
