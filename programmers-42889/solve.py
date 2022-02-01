def get_fail_ratio(not_cleared_number, reached_number):
    if reached_number == 0:
        return 0
    return not_cleared_number / reached_number


def solution(N, stages):
    numbers_per_stage = [0 for x in range(N + 1)]

    for stage in stages:
        numbers_per_stage[stage - 1] += 1

    answer = []
    for index, numbers in enumerate(numbers_per_stage[:len(numbers_per_stage) - 1]):
        reached_number = sum(numbers_per_stage[index:])
        not_cleared_number = numbers
        answer.append((get_fail_ratio(not_cleared_number, reached_number), index + 1))

    answer.sort(key=lambda x: x[0], reverse=True)

    return [x[1] for x in answer]
