# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


l14 = ListNode(4)
l12 = ListNode(2)
l12.next = l14
l11 = ListNode(1)
l11.next = l12

l24 = ListNode(4)
l23 = ListNode(3)
l23.next = l24
l21 = ListNode(1)
l21.next = l23

s = Solution()
rlst=s.mergeTwoLists(l11, l21)
print(rlst)
