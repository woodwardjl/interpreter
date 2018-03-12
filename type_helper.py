
def is_operator(value: str) -> bool:
    return value in ["mult", "div", "plus", "minus"]

def is_comparison(value: str) -> bool:
    return value in ["gt", "lt", "gteq", "lteq", "iseq", "noteq"]