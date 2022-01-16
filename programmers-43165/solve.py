cnt = 0


def traverse(numbers, index, target, current):
    global cnt

    if index == len(numbers):
        if current == target:
            cnt += 1
        return

    traverse(numbers, index + 1, target, current + numbers[index])
    traverse(numbers, index + 1, target, current - numbers[index])


def solution(numbers, target):
    global cnt

    traverse(numbers, 0, target, 0)

    return cnt
