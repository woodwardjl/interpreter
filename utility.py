from collections import defaultdict


def make_default_dict(default_value, pairs: [()]) -> defaultdict:
    map = defaultdict(lambda: default_value)
    for k, v in pairs:
        map[k] = v

    return map

def replace_in_list(check_list, to_find, replacement):
    for index, item in enumerate(check_list):
        if type(item) == list:
            replace_in_list(item, to_find, replacement)
        else:
            if item == to_find:
                check_list[index] = replacement
