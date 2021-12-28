def solution(m, n, puddles):
    PUDDLE = -987654321
    l = [[1] * m]

    for i in range(n - 1):
        l.append([1] + [0] * (m - 1))

    for puddle in puddles:
        l[puddle[1] - 1][puddle[0] - 1] = PUDDLE

        if puddle[0] - 1 == 0:
            for i in range(puddle[1], n):
                l[i][puddle[0] - 1] = PUDDLE
        if puddle[1] - 1 == 0:
            for i in range(puddle[0], n):
                l[puddle[1] - 1][i] = PUDDLE
        if puddle[0] - 1 == 0 and puddle[1] - 1 == 0:
            l[1] = [l[1][0]] + [1] * m
            for i in range(1, n):
                l[i][1] = 1

    for i in range(1, n):
        for j in range(1, m):
            if l[i][j] < 0:
                continue
            up = max(l[i - 1][j], 0)
            left = max(l[i][j - 1], 0)
            l[i][j] = (l[i][j] % 1000000007 + up % 1000000007 + left % 1000000007) % 1000000007

    # for i in l:
    #     print(i)

    return l[n - 1][m - 1]


print(solution(10, 10, [[1, 1]]))
