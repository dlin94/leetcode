# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        elif not head.next:
            if head.val == val:
                return None
            else:
                return head


        while head and head.val == val:
            head.next, head = None, head.next

        curr = head
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            if curr.next and curr.next.val != val:
                curr = curr.next
            elif not curr.next:
                curr = curr.next
        return head
