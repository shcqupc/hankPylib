#####################################################
# 反转一个单链表。
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#####################################################
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def printList(self, tmp):
        while tmp:
            print(str(tmp.val), '->', sep="", end="")
            if tmp.next is None:
                print("NULL")
                break
            tmp = tmp.next
#####################################################
# iteration
#####################################################
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

#####################################################
# regression
#####################################################
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        temp = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return temp

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)
n1.next.next.next.next = ListNode(5)
n2 = ListNode(3)
n2.next = ListNode(2)
n2.next.next = ListNode(5)

s = Solution()
s.printList(n1)
# s.printList(s.reverseList1(n1))
s.printList(s.reverseList2(n1))
