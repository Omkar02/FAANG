# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')
from collections import Counter
import heapq as h


def sort_By_Freq(s):
    heap, cnt = [], Counter(s)
    ret = ''
    for key in cnt:
        h.heappush(heap, (-cnt[key], key))
    while len(heap) > 0:
        cur = h.heappop(heap)
        ret += cur[1] * (-cur[0])
    return ret


s = 'tree'
print(sort_By_Freq(s))
