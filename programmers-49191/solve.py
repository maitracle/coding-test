from collections import deque


def solution(n, results):
    graph = [[0 for _ in range(n)] for __ in range(n)]

    for result in results:
        graph[result[0] - 1][result[1] - 1] = 1
        graph[result[1] - 1][result[0] - 1] = -1

    for node in range(n):
        losers = deque([target_node for target_node, result in enumerate(graph[node]) if result == 1])

        while losers:
            looser = losers.popleft()
            for j in range(n):
                if graph[looser][j] == 1 and graph[node][j] == 0:
                    losers.append(j)
                    graph[node][j] = 1
                    graph[j][node] = -1

    ans = 0

    for i in graph:
        if i.count(0) == 1:
            ans += 1

    return ans
