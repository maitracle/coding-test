def to_map_string(n, number):
    output = ''
    while True:
        if number == 1:
            output = '#' + output
            break
        elif number == 0:
            output = ' ' + output
            break
        elif number % 2 == 1:
            output = '#' + output
            number = int(number / 2)
        else:
            output = ' ' + output
            number = int(number / 2)
    return (n - len(output)) * ' ' + output


def solution(n, arr1, arr2):
    map_1 = ''
    map_2 = ''

    for i in arr1:
        map_1 += to_map_string(n, i)
    for i in arr2:
        map_2 += to_map_string(n, i)

    result = ''
    for i, j in zip(map_1, map_2):
        result += ' ' if (i == ' ' and j == ' ') else '#'

    answer = [result[i: i + n] for i in range(0, len(result), n)]
    return answer