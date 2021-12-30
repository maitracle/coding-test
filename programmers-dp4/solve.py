def solution(money):
    money_length = len(money)
    dp_map = [[0 for _ in range(money_length)] for _ in range(2)]

    for i in range(2):
        for j in range(len(money) - 1):
            dp_map[i][(i + j) % money_length] = max(
                dp_map[i][(i + j - 2) % money_length] + money[(i + j) % money_length],
                dp_map[i][(i + j - 1) % money_length]
            )

    return max(dp_map[0][money_length - 2], dp_map[1][money_length - 1])
