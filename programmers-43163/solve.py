min_length = 987654321


def is_connected(word1, word2):
    diff_cnt = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff_cnt += 1

    return diff_cnt <= 1


def solution(begin, target, words):
    global min_length
    whole_words = [begin, *words]
    connection_graph = [[False for x in whole_words] for y in whole_words]
    is_visited = [False for y in whole_words]

    for index1, word1 in enumerate(whole_words):
        for index2, word2 in enumerate(whole_words):
            connection_graph[index1][index2] = is_connected(word1, word2)

    def dfs(index, length):
        global min_length
        if whole_words[index] == target:
            min_length = min(min_length, length)
            return
        if is_visited[index] is True:
            return

        is_visited[index] = True

        for next_node_index in range(len(connection_graph)):
            if connection_graph[index][next_node_index] and is_visited[next_node_index] is False:
                dfs(next_node_index, length + 1)

    dfs(0, 0)

    if min_length == 987654321:
        return 0

    return min_length
