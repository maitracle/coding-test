import itertools
from functools import reduce


def is_prime(number):
    return number > 1 and reduce(lambda acc, cur: (number % cur != 0) and acc, range(2, int(number ** 0.5) + 1), True)


def solution(numbers):
    prime_map = {}
    answer = 0

    for length in range(1, len(numbers) + 1):
        permutations = itertools.permutations(numbers, length)

        for permutation in permutations:
            number = int(reduce(lambda acc, cur: acc + cur, permutation, ''))

            if is_prime(number) and not (number in prime_map):
                answer += 1
                prime_map[number] = True

    return answer
