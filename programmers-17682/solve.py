def refine_result(result):
    result = result.replace('10', 'A')
    chance_chars = []
    current = ''
    for char in result:
        if char.isnumeric() or char == 'A':
            chance_chars.append(current)
            current = '' + char
        else:
            current += char

    chance_chars = chance_chars[1:] + [current]

    chances = []

    for chance_char in chance_chars:
        point = 10 if chance_char[0] == 'A' else int(chance_char[0])
        bonus = chance_char[1]
        option = '-' if len(chance_char) == 2 else chance_char[2]

        chances.append((point, bonus, option))

    return chances


def calc_points(chance):
    [point, bonus, option] = chance
    bonus_map = {
        'S': 1,
        'D': 2,
        'T': 3,
    }

    if option == '#':
        return - point ** bonus_map[bonus]

    return point ** bonus_map[bonus]


def solution(dartResult):
    dart_result = dartResult

    chances = refine_result(dart_result)

    ans_list = [0, 0, 0]
    for index, chance in enumerate(chances):
        ans_list[index] = calc_points(chance)

        if chance[2] == '*':
            ans_list[index] += ans_list[index]

            if index != 0:
                ans_list[index - 1] += ans_list[index - 1]

    return sum(ans_list)
