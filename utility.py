from collections import defaultdict


def make_default_dict(default_value, pairs: [()]) -> defaultdict:
    map = defaultdict(lambda: default_value)
    for k, v in pairs:
        map[k] = v

    return map
