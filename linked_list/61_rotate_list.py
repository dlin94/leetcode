# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        end = head
        length = 1
        while end and end.next:
            if end.next.next:
                end = end.next.next
                length += 2
            else:
                end = end.next
                length += 1

        k = k % length
        i = 1
        curr = head
        while i < length - k:
            i += 1
            curr = curr.next

        if end != curr:
            end.next, curr.next, head = head, None, curr.next

        return head
