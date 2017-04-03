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
        if not head:
            return

        head, head.next = ListNode(0), head
        p = head # behind n
        n = head.next # in front of p
        dup = None
        while n.next:
            if n.next.val == n.val:
                p.next, n = n.next, n.next
                dup = n.val
            elif n.val == dup:
                p.next, n = n.next, n.next
            else:
                p, n = n, n.next

        print(p.val, n.val, dup)
        if n.val == dup:
            p.next = None

        return head.next
