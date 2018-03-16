class Node(object):
    __slots__ = "key", "value", "left_child", "right_child", "factor"

    def __init__(self, key: int, value: int or str,
                 left_child, right_child, factor=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.factor = factor

    @staticmethod
    def create(key: int, value: int, left_child=None,
               right_child=None, factor=None):
        return Node(key, value, left_child, right_child, factor)

    def is_leaf(self) -> bool:
        return self.left_child == None and self.right_child == None

    def set_values(self, key: int, value: int):
        self.key = key
        self.value = value

    def has_both_children(self) -> bool:
        return self.left_child != None and self.right_child != None

    def __str__(cls):
        has_right_child = cls.right_child != None
        has_left_child = cls.left_child != None

        return "{} -> {}, {}{}{}".format(
                cls.key,
                cls.left_child.key if has_left_child else "LEAF",
                cls.right_child.key if has_right_child else "LEAF",
                "\n" + str(cls.left_child) if has_left_child else "",
                "\n" + str(cls.right_child) if has_right_child else "")


if __name__ == "__main__":
    print(Node(5, "Five", None, None, 0))
