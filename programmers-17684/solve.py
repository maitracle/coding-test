from collections import deque


def solution(msg):
    dictionary = {}

    for index, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        dictionary[char] = index + 1
    last_index = 26

    answer = []
    current = ''

    q = deque(msg)

    while q:
        char = q.popleft()

        if current + char in dictionary:
            current += char
            continue
        else:
            answer.append(dictionary[current])
            current += char
            last_index += 1
            dictionary[current] = last_index
            current = ''
            q.appendleft(char)

    answer.append(dictionary[current])
    return answer
