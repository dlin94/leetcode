# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # Determine the midpoint of the list
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev, slow = slow, slow.next
            fast = fast.next.next

        # Temporarily split up both lists.
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left, right):
        lp = left
        rp = right

        head = None
        if lp.val < rp.val:
            head, lp = lp, lp.next
            head.next = None
        else:
            head, rp = rp, rp.next
            head.next = None

        merged = head
        while lp and rp:
            if lp.val < rp.val:
                merged.next, lp = lp, lp.next
            else:
                merged.next, rp = rp, rp.next
            merged = merged.next
            merged.next = None

        if not lp:
            merged.next = rp
        else:
            merged.next = lp

        return head
