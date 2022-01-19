from collections import defaultdict


def solution(tickets):
    routes = defaultdict(list)

    for start, dest in tickets:
        routes[start].append(dest)

    for start in routes:
        routes[start].sort()

    def dfs(start, footprint):
        if len(footprint) == len(tickets) + 1:
            return footprint

        for index, dest in enumerate(routes[start]):
            routes[start].pop(index)

            ret = dfs(dest, [*footprint, dest])
            if ret: return ret

            routes[start].insert(index, dest)

    return dfs("ICN", ["ICN"])
