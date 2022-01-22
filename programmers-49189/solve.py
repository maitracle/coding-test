from collections import deque


def solution(n, edge):
    graph = {}
    distances = [987654321 for x in range(n)]
    distances[0] = 0
    q = deque([0])

    for i in edge:
        node1 = i[0] - 1
        node2 = i[1] - 1

        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if distances[next_node] == 987654321:
                q.append(next_node)
                distances[next_node] = distances[node] + 1

    return distances.count(max(distances))
