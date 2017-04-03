# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head or not head.next or m == n:
            return head

        curr = head
        before = None
        after = None
        i = 1
        new = None
        end = None
        while True:
            if i == m - 1:
                before = curr
                curr = curr.next
            elif i >= m and i <= n:
                if i == m:
                    end = curr
                if i == n:
                    after = curr.next
                    curr.next, curr, new = new, curr.next, curr
                    break
                else:
                    curr.next, curr, new = new, curr.next, curr
            else:
                curr = curr.next
            i += 1

        if before:
            before.next = new
        end.next = after

        if before:
            return head
        else:
            return new
