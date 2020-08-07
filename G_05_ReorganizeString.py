import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Heap', Difficult='Hard')


import heapq


def __lt__(self, other):
    return one[0] < other[0]


def reorganizeString(string):
    counts = [(-string.count(i), i) for i in set(string)]
    heapq.heapify(counts)
    if any(-nc > (len(string) + 1) / 2 for nc, x in counts):
        return "Cant be done!"
    ans = []
    while len(counts) >= 2:
        remainingCaharOne, characterOne = heapq.heappop(counts)
        remainingCaharTwo, characterTwo = heapq.heappop(counts)
        ans.append(characterOne)
        ans.append(characterTwo)
        if remainingCaharOne + 1:
            heapq.heappush(counts, (remainingCaharOne + 1, characterOne))
        if remainingCaharTwo + 1:
            heapq.heappush(counts, (remainingCaharTwo + 1, characterTwo))

    return ''.join(ans) + (counts[0][1] if counts else '')


string = 'abbca'
print(reorganizeString(string))
