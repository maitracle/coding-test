def solution(record):
    nickname_map = {}

    result = []
    for i in record:
        split = i.split()

        if len(split) == 3:
            nickname_map[split[1]] = split[2]

    for i in record:
        split = i.split()
        if split[0] == 'Enter':
            result.append(f'{nickname_map[split[1]]}님이 들어왔습니다.')
        elif split[0] == 'Leave':
            result.append(f'{nickname_map[split[1]]}님이 나갔습니다.')

    return result
