import string

tmp = string.digits + string.ascii_uppercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    result = ''

    base = 0
    answer = ''
    index = p - 1
    cnt = 0
    while cnt < t:
        while len(result) <= index:
            result += convert(base, n)
            base += 1

        answer += result[index]
        cnt += 1
        index += m

    return answer
