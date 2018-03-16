import operator


def lteq(left: int, right: int) -> bool:
    return operator.lt(left, right) or operator.eq(left, right)


def gteq(left: int, right: int) -> bool:
    return operator.gt(left, right) or operator.eq(left, right)


def noteq(left: int, right: int) -> bool:
    return not operator.eq(left, right)


def max(left: int, right: int) -> int:
    return left if left > right else right


def min(left: int, right: int) -> int:
    return left if left < right else right
