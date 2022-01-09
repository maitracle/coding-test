def solution(n, lost, reserve):
    redundancies = set(reserve) - set(lost)
    starvings = set(lost) - set(reserve)

    for redundancy in redundancies:
        if redundancy - 1 in starvings:
            starvings.remove(redundancy - 1)
        elif redundancy + 1 in starvings:
            starvings.remove(redundancy + 1)

    return n - len(starvings)
