def is_basic_math(value: str) -> bool:
    return value in ["mult", "div", "plus", "minus", "pow", "mod",
                     "max", "min"]


def is_advanced_math(value: str) -> bool:
    return value in ["abs", "factorial", "sqrt", "neg"]

def is_math(value: str) -> bool:
    return is_basic_math(value) or is_advanced_math(value)


def is_operator(value: str) -> bool:
    return value in ["gt", "lt", "gteq", "lteq", "iseq", "noteq", "and"]

def is_keyword(value: str) -> bool:
    return is_basic_math(value) or \
           is_advanced_math(value) or \
           is_operator(value) or \
           value in ["begin", "define", "put"]


def is_string(value: str) -> bool:
    if len(value) < 2:
        return False

    return (value[0] == "'" and value[len(value) -1] == "'") or \
           (value[0] == "\"" and value[len(value) - 1] == "\"")
