def solution(numbers):
    chars = [str(i) for i in numbers]
    chars.sort(key=lambda x: x * 3, reverse=True)
    answer = ''

    for i in chars:
        answer += i

    return str(int(answer))
