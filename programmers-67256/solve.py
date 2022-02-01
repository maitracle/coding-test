def get_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def solution(numbers, hand):
    position = {
            1: [0, 3],
            2: [1, 3],
            3: [2, 3],
            4: [0, 2],
            5: [1, 2],
            6: [2, 2],
            7: [0, 1],
            8: [1, 1],
            9: [2, 1],
            '*': [0, 0],
            0: [1, 0],
            '#': [2, 0],
    }
    thumb = {
            'L': '*',
            'R': '#',
    }

    answer = ''

    for number in numbers:
        l_dist = get_distance(position[thumb['L']], position[number])
        r_dist = get_distance(position[thumb['R']], position[number])

        print(number, l_dist, r_dist)

        if number in [1, 4, 7]:
            answer += 'L'
            thumb['L'] = number
        elif number in [3, 6, 9]:
            answer += 'R'
            thumb['R'] = number
        else:
            if hand == 'left':
                if l_dist <= r_dist:
                    answer += 'L'
                    thumb['L'] = number

                else:
                    answer += 'R'
                    thumb['R'] = number
            else:
                if l_dist < r_dist:
                    answer += 'L'
                    thumb['L'] = number
                else:
                    answer += 'R'
                    thumb['R'] = number
    return answer
