import itertools


def is_candidate(item_counts, set_items):
    return item_counts == len(set_items)


def get_item_with_keys(item, keys):
    output = ''
    for key in keys:
        output += item[key]

    return output


def solution(relation):
    candidates = []
    key_counts = len(relation[0])
    not_yet_candidates = [x for x in range(0, key_counts)]

    for count in range(1, key_counts + 1):
        for keys in itertools.combinations(not_yet_candidates, count):
            keys_are_valid = True
            for candidate in candidates:
                if candidate.issubset(set(keys)):
                    keys_are_valid = False
                    break

            if not keys_are_valid:
                continue

            set_items = set()

            for item in relation:
                set_items.add(get_item_with_keys(item, keys))

            if is_candidate(len(relation), set_items):
                candidates.append(set(keys))

    return len(candidates)
