def get_time_from_string(time):
    hour, minute, second_origin = time.split(':')
    second, milli_second = second_origin.split('.')

    return (int(hour) * 3600 + int(minute) * 60 + int(second)) * 1000 + int(milli_second)


def get_item_from_second_string(second):
    without_s = second[:len(second) - 1]

    if '.' in without_s:
        split_with_dot = without_s.split('.')

        return int(split_with_dot[0]) * 1000 + int(split_with_dot[1])
    else:
        return int(without_s) * 1000


def get_start_end(line):
    date, end_time_string, duration_string = line.split()
    end_time = get_time_from_string(end_time_string)
    return (
        end_time - get_item_from_second_string(duration_string) + 1,
        end_time,
    )


def is_out(number1, number2):
    return number2 < number1


def solution(lines):
    refined = []
    max_throughput = 0

    for line in lines:
        refined.append(get_start_end(line))

    for current in refined:
        max_throughput = max(
            max_throughput,
            count_throughput(refined, current[1], current[1] + 1000),
        )
    return max_throughput


def count_throughput(refined, start, end):
    throughput = 0
    for i in refined:
        if i[1] >= start and i[0] < end:
            throughput += 1

    return throughput