def solution(citations):
    citations.sort(reverse=True)

    for index, value in enumerate(citations):

        if index >= value:
            return index

    return len(citations)
