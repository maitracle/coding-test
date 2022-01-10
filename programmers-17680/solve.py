def solution(cacheSize, cities):
    queue = []
    time = 0

    for city in cities:
        city_lowcase = city.lower()
        if city_lowcase in queue:
            time += 1
            queue = list(filter(lambda x: x != city_lowcase, queue))
            queue.insert(0, city_lowcase)
        else:
            time += 5
            queue.insert(0, city_lowcase)
            queue = queue[0: cacheSize]

    return time