def replace_in_list(check_list: list, to_find, replacement):
    for index, item in enumerate(check_list):
        if type(item) == list:
            replace_in_list(item, to_find, replacement)
        else:
            if item == to_find:
                check_list[index] = replacement


def replace_in_str(check_string: str, to_find: str, replacement: str) -> str:
    return check_string.replace(to_find, replacement)


def is_two_different_types(t: type, fst, snd) -> bool:
    return (type(fst) == t and type(snd) != t) \
           or (type(fst) != t and type(snd) == t)


def is_char(char, checker) -> bool:
    return char == checker


def is_list_of_lists(check_list: list) -> bool:
    if check_list == []:
        return False

    return type(check_list[0]) == list
