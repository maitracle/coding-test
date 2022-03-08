import string

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    for number in map(lambda x: int(x), filter(lambda x: x != '', str(convert(n, k)).split('0'))):
        if is_prime(number):
            answer += 1

    return answer
