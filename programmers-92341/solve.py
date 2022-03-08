import math


def calc_time_delta(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    in_minute += in_hour * 60
    out_hour, out_minute = map(int, out_time.split(":"))
    out_minute += out_hour * 60

    return out_minute - in_minute


def calc_fee(minutes, fees):
    basic_minutes, basic_price, unit_minute, unit_price = fees

    extra_minutes = max(minutes - basic_minutes, 0)
    extra_price = math.ceil(extra_minutes / unit_minute) * unit_price

    return basic_price + extra_price


def calc_total_minutes_and_calc_fee(histories, fees):
    minutes = 0
    for history in [histories[i: i + 2] for i in range(0, len(histories), 2)]:
        minutes += calc_time_delta(*history)

    return calc_fee(minutes, fees)


def solution(fees, records):
    car_time_logs = {}

    for record in records:
        time, car_number, action = record.split()
        if car_number in car_time_logs:
            car_time_logs[car_number].append(time)
        else:
            car_time_logs[car_number] = [time]

    for key in car_time_logs:
        if len(car_time_logs[key]) % 2 == 1:
            car_time_logs[key].append('23:59')

    answer = []
    for key in sorted(car_time_logs.keys()):
        answer.append(calc_total_minutes_and_calc_fee(car_time_logs[key], fees))

    return answer
