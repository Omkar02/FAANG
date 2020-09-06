# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


def sequenceReconstruction(org, seqs):
    """
    :type org: List[int]
    :type seqs: List[List[int]]
    :rtype: bool
    """
    indexes = {e: i for i, e in enumerate(org)}
    print(f'indexes = {indexes}')
    edges = set()

    if not seqs:
        return False
    for seq in seqs:
        print(f'\t{seq}')
        for s in seq:
            print(f'\t\t{s}')
            if s not in indexes:
                print(f'\t\t\tFalse')
                return False
        for i in range(1, len(seq)):
            print(f'\t\t{i}')
            pre, cur = seq[i - 1], seq[i]
            if indexes[pre] > indexes[cur]:
                return False
            print(f'\t\t{edges}')
            edges.add((pre, cur))
        print('\t===========================')

    print(edges)

    for x in range(1, len(org)):
        print(f'\t{(org[x - 1], org[x])}')
        if (org[x - 1], org[x]) not in edges:
            print(f'\t\tFalse')
            return False

    return True


org = [1, 2, 3]
seqs = [[1, 2], [1, 3], [2, 3]]


org = [1, 2, 3]
seqs = [[1, 2]]

# org = [4, 1, 5, 2, 6, 3]
# seqs = [[5, 2, 6, 3], [4, 1, 5, 2]]

print(sequenceReconstruction(org, seqs))
