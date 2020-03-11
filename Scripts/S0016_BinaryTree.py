from __future__ import annotations

from typing import Union
from collections import deque


class TreeNode:
    def __init__(self, value, l_node: TreeNode = None, r_node: TreeNode = None):
        self.value = value
        self.l_node = l_node
        self.r_node = r_node

    def printself(self, height, preStr, length):
        if not self:
            return

        string = preStr + str(self.value) + preStr
        leftLen = (length - len(string)) // 2
        rightLen = length - len(string) - leftLen
        res = " " * leftLen + string + " " * rightLen
        print(" " * height * length + res)
        if self.l_node:
            self.l_node.printself(height + 1, '^', length)
        if self.r_node:
            self.r_node.printself(height + 1, 'v', length)


def gen_tree(values: list) -> Union[TreeNode, None]:
    if not values:
        return None
    iter_value = iter(values)
    root = TreeNode(next(iter_value))
    d = deque()
    d.append(root)
    while 1:
        head = d.popleft()
        try:
            head.l_node = TreeNode(next(iter_value))
            d.append(head.l_node)
            head.r_node = TreeNode(next(iter_value))
            d.append(head.r_node)
        except StopIteration:
            break
    return root


def pre_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield node.value
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)


def in_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield from pre_traverse_tree(node.l_node)
    yield node.value
    yield from pre_traverse_tree(node.r_node)


def post_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)
    yield node.value


tree = gen_tree(list(range(10)))
print(list(pre_traverse_tree(tree)))
print(list(in_traverse_tree(tree)))
print(list(post_traverse_tree(tree)))

tree.printself(0, 'H', 5)