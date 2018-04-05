import operator as o


def lteq(left: int, right: int) -> bool:
    return o.lt(left, right) or o.eq(left, right)


def gteq(left: int, right: int) -> bool:
    return o.gt(left, right) or o.eq(left, right)


def noteq(left: int, right: int) -> bool:
    return not o.eq(left, right)


def max(left: int, right: int) -> int:
    return left if left > right else right


def min(left: int, right: int) -> int:
    return left if left < right else right
