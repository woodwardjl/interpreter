
def is_basic_math(value: str) -> bool:
    return value in ["mult", "div", "plus", "minus", "pow", "mod",
                     "max", "min"]

def is_advanced_math(value: str) -> bool:
    return value in ["abs", "factorial", "sqrt", "neg"]

def is_operator(value: str) -> bool:
    return value in ["gt", "lt", "gteq", "lteq", "iseq", "noteq", "and"]