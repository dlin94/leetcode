# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        dummy, dummy.next = ListNode(0), head
        prev, prev.next = dummy, dummy.next
        while curr and curr.next:
            prev.next, curr.next.next, curr.next = curr.next, curr, curr.next.next
            curr, prev = curr.next, curr
        return dummy.next
