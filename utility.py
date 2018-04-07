from collections import defaultdict


def make_default_dict(default_value, pairs: [()]) -> defaultdict:
    map = defaultdict(lambda: default_value)
    for k, v in pairs:
        map[k] = v

    return map


def replace_in_list(check_list: list, to_find, replacement):
    for index, item in enumerate(check_list):
        if type(item) == list:
            replace_in_list(item, to_find, replacement)
        else:
            if item == to_find:
                check_list[index] = replacement


def replace_in_str(check_string: str, to_find: str, replacement: str) -> str:
    return check_string.replace(to_find, replacement)


def is_char(char, checker) -> bool:
    return char == checker


def is_different_numeric_type(fst: int or float, snd: int or float) -> bool:
    return (type(fst) == int and type(snd) == float) \
           or (type(snd) == float and type(snd) == int)