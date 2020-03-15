from typing import Union
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printself(self, height, preStr, length):
        if not self:
            return
        # print(self.val)
        # if self.left:
        #     self.left.printself()
        # if self.right:
        #     self.right.printself()
        string = preStr + str(self.val) + preStr
        leftLen = (length - len(string)) // 2
        rightLen = length - len(string) - leftLen
        res = " " * leftLen + string + " " * rightLen
        print(" " * height * length + res)
        if self.left:
            self.left.printself(height + 1, '^', length)
        if self.right:
            self.right.printself(height + 1, 'v', length)


def gen_tree(root, llist, i):
    if i < len(llist):
        if not llist[i]:
            return None  # 这里的return很重要
        else:
            root = TreeNode(llist[i])
            # print(i)
            root.left = gen_tree(root.left, llist, 2 * i + 1)
            root.right = gen_tree(root.right, llist, 2 * i + 2)
            return root  # 这里的return很重要
    return root


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        #执行用时 : 24 ms , 在所有 Python 提交中击败了 97.56% 的用户
        #内存消耗 : 15.8 MB , 在所有 Python 提交中击败了 5.41% 的用户

        :type root: TreeNode
        :rtype: int
        """

        def getdiam(root):
            if not root:
                return 0, 0
            l_depth, l_diam = getdiam(root.left)
            r_depth, r_diam = getdiam(root.right)
            return max(l_depth, r_depth) + 1, max(l_depth + r_depth, l_diam, r_diam)

        depth, diam = getdiam(root)
        return max(depth - 1, diam)

root = TreeNode(0)
llist = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1,
         -4,
         None, None, None, -2]
tree = gen_tree(root, llist, 0)
# tree.printself(0, 'H', 5)
s = Solution()
print(s.diameterOfBinaryTree(tree))

tn = TreeNode(1)
tn.left = TreeNode(2)
tn.right = TreeNode(3)
tn.left.left = TreeNode(4)
tn.left.right = TreeNode(5)
tn.left.right.left = TreeNode(6)
# tn.printself(0, 'H', 5)
# print(s.diameterOfBinaryTree(tn))
