N = int(input())

points = [0]
dp_map = [0] * (N + 2)

for i in range(N):
    points.append(int(input()))

dp_map[1] = points[1]
dp_map[2] = points[1] + points[2]
dp_map[3] = max(points[1] + points[3], points[2] + points[3])


def solve(n):
    if dp_map[n] == 0:
        dp_map[n] = max(solve(n - 3) + points[n - 1] + points[n], solve(n - 2) + points[n])

    return dp_map[n]


print(solve(N))
