visited = []
connections = []


def check_network(index):
    global visited
    global connections
    visited[index] = True

    for next_node_index in range(len(connections)):
        if connections[index][next_node_index] and not visited[next_node_index]:
            print('inin')
            check_network(next_node_index)

    print('leave', index)


def solution(n, computers):
    global visited
    global connections
    visited = [False for i in range(n)]
    connections = computers

    cnt = 0
    for index, is_visited in enumerate(visited):
        if is_visited is False:
            check_network(index)
            cnt += 1

    return cnt
