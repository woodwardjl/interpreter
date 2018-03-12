import operator

def lteq(left: int, right: int) -> bool:
    return operator.lt(left, right) or operator.eq(left, right)

def gteq(left: int, right: int) -> bool:
    return operator.gt(left, right) or operator.eq(left, right)

def noteq(left: int, right: int) -> bool:
    return not operator.eq(left, right)
