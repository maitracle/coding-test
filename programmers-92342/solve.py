from collections import deque


def solution(n, info):
    def calc_points_diff(own_footprint, counterpart_footprint):
        point = 0
        counterpart_point = 0
        for index, (own, counterpart) in enumerate(zip(own_footprint, counterpart_footprint)):
            if own == 0 and counterpart == 0:
                continue
            if own > counterpart:
                point += 10 - index
            else:
                counterpart_point += 10 - index

        return point - counterpart_point

    q = deque([
        [0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ])
    max_diff = 0
    answer = [-1]

    while len(q):
        current_index, footprint = q.popleft()

        used_arrows = sum(footprint)

        if used_arrows == n:
            diff = calc_points_diff(footprint, info)

            if diff and diff >= max_diff:
                max_diff = diff
                answer = footprint[:]
            continue

        elif used_arrows > n:
            continue

        elif current_index == 11:
            rest_arrow = n - used_arrows
            if rest_arrow > 0:
                shoot_footprint = footprint[:]
                shoot_footprint[10] += rest_arrow
                q.append([current_index, shoot_footprint[:]])
            continue

        shoot_footprint = footprint[:]
        shoot_footprint[current_index] += info[current_index] + 1

        q.append([current_index + 1, shoot_footprint[:]])
        q.append([current_index + 1, footprint[:]])

    return answer
