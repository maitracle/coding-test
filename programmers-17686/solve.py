import re


def solution(files):
    refined = []

    for file in files:

        split_head = re.split('(\d+)', file)
        letters = split_head[0].lower()
        number = None

        if len(split_head) >= 2 and split_head[1].isnumeric():
            number = int(split_head[1])

        refined.append({
            'origin': file,
            'letters': letters,
            'number': number
        })

    refined.sort(key=lambda x: (x['letters'], x['number']))

    answer = []
    for i in refined:
        answer.append(i['origin'])

    return answer
