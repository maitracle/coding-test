def solution(brown, yellow):
    answer = []

    block_cnt = int(brown / 2) + 1
    max_height = int(brown / 4) + 1

    for height in range(3, max_height + 1):
        width = block_cnt - height + 1
        y_width = width - 2
        y_height = height - 2

        if yellow == y_width * y_height:
            return [width, height]

    return answer
