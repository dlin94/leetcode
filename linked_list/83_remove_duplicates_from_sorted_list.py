# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head, head.next = ListNode(-1), head
        curr = head
        while curr.next:
            if curr.next.val == curr.val and curr != head:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head.next
