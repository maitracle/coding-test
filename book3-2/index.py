n, m = map(int, input().split())

values = []

for i in range(n):
    values.append(map(int, input().split()))

ans = 0

for i in range(n):
#     local_min = 10001
    local_min = min(values[i])
#     for j in values[i]:
#         if local_min > j:
#             local_min = j

    if ans < local_min:
        ans = local_min

print(ans)
