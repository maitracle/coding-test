N = int(input())

points = [0 for _ in range(301)]
dp_map = [0 for _ in range(301)]

for i in range(N):
    points[i] = int(input())

dp_map[0] = points[0]
dp_map[1] = points[0] + points[1]
dp_map[2] = max(points[0] + points[2], points[1] + points[2])


for i in range(3, N):
    dp_map[i] = max(dp_map[i - 3] + points[i - 1] + points[i], dp_map[i - 2] + points[i])

print(dp_map[N - 1])
