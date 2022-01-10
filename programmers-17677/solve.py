from collections import Counter


def refine_input(string):
    lower_str = string.lower()

    output = []
    for i, j in zip(lower_str, lower_str[1:]):
        if i.isalpha() and j.isalpha():
            output.append(i + j)

    return Counter(output)


def get_length(counter):
    return len(list(counter.elements()))


def solution(str1, str2):
    counter1 = refine_input(str1)
    counter2 = refine_input(str2)

    if get_length(counter1 | counter2) == 0:
        return 65536

    else:
        return int((get_length(counter1 & counter2) / get_length(counter1 | counter2)) * 65536)
