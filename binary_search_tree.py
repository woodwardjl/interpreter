from node import Node


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root
        self.elements = 0

    def search(self, key: int) -> str or None:
        current = self.root

        while current:
            if key == current.key:
                return current.value
            else:
                current = current.left_child \
                    if key < current.key else current.right_child

        return None

    def insert(self, key: int, value: int or str) -> "BinarySearchTree":
        if self.root == None:
            self.root = Node.create(key, value)
            return self

        current = self.root

        while current != None:
            if key == current.key:
                current.value = value
                return self
            else:
                if key < current.key:
                    if current.left_child == None:
                        current.left_child = Node.create(key, value,
                                                         None, None)
                        return self
                    else:
                        current = current.left_child
                else:
                    if current.right_child == None:
                        current.right_child = Node.create(key, value,
                                                          None, None)
                    else:
                        current = current.right_child

        return self

    def remove(self, key: int) -> "BinarySearchTree":
        if self.root.is_leaf():
            if self.root.key == key:
                self.root = None
        else:
            self.__remove(key, self.root, None)
        return self

    def __remove(self, key: int, current: Node, parent: Node or None) -> None:
        if parent is None and key == current.key:
            self.__delete_root()
            return

        while current != None:
            if key == current.key:
                if current.is_leaf():
                    self.__delete_leaf(current, parent)
                elif not current.has_both_children():
                    self.__delete_with_one_child_only(current, parent)
                    return
                else:
                    min = self.__min(current.right_child)
                    current.set_values(min.key, min.value)
                    self.__remove(current.key, current.right_child, current)
            else:
                parent = current
                current = (current.left_child
                           if key < current.key
                           else current.right_child)

    def __delete_root(self) -> None:
        if self.root.right_child is not None:
            self.root = self.root.right_child
        else:
            self.root = self.root.left_child

    def __delete_leaf(self, current: Node, parent: Node):
        if parent.left_child == current:
            parent.left_child = None
        else:
            parent.right_child = None
        return

    def __delete_with_one_child_only(self, current: Node,
                                     parent: Node) -> None:
        if parent.left_child == current:
            if current.left_child == None:
                parent.left_child = current.right_child
            else:
                parent.left_child = current.left_child
        else:
            if current.left_child == None:
                parent.right_child = current.right_child
            else:
                parent.right_child = current.left_child

    def __min(self, node: Node) -> Node:
        while node.left_child != None:
            node = node.left_child
        return node

    def __str__(cls):
        return str(cls.root)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10, "Ten").insert(5, "Five").insert(3, "Three") \
        .insert(7, "Seven").insert(9, "Nine").insert(4, "Four").remove(5)
    print(bst)
