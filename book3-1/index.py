n, m, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))
numbers.sort(reverse=True)


big = int(m / (k + 1)) * k
big += m % (k + 1)

small = m - big

print(numbers)
print(big, small)

ans = big * numbers[0] + small * numbers[1]

print(ans)

# ans = 0
# limit = 0
# for i in range(1, m + 1):
#     if i % k == 0:
#         ans += numbers[1]
#         limit = 0
#     else:
#         ans += numbers[0]
#         limit += 1
#
# print(ans)