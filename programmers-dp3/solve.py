def solution(m, n, puddles):
    map = [[0] * (m + 1) for i in range(n + 1)]
    map[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = (map[i - 1][j] + map[i][j - 1]) % 1000000007

    return map[n][m]