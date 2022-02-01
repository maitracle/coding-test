import copy
import itertools
from collections import deque


def calc(value1, value2, operator):
    num1 = int(value1)
    num2 = int(value2)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def solution(expression):
    operator_order = ['+', '-', '*']

    splitted = deque([])
    temp = ''
    for i in expression:
        if i.isnumeric():
            temp += i
        else:
            splitted.append(int(temp))
            splitted.append(i)
            temp = ''
    splitted.append(int(temp))

    maximum = 0
    for order in itertools.permutations(operator_order, 3):
        origin = copy.deepcopy(splitted)

        for operator in order:
            stack = deque([])
            while origin:
                value = origin.popleft()
                if value == operator:
                    left = stack.pop()
                    right = origin.popleft()
                    stack.append(calc(left, right, operator))
                else:
                    stack.append(value)
            origin = stack
        maximum = max(maximum, abs(int(origin[0])))

    return maximum
