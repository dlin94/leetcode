# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev = head
        curr = head.next
        while curr is not None:
            if curr.val < prev.val:
                if curr.val < head.val:
                    curr.next, prev.next, head, curr = head, curr.next, curr, curr.next
                else:
                    sort_prev = head
                    sort_curr = head.next
                    while curr.val > sort_curr.val and prev != sort_curr:
                        sort_prev = sort_prev.next
                        sort_curr = sort_curr.next
                    sort_prev.next, curr.next, prev.next, curr = curr, sort_curr, curr.next, curr.next
            else:
                curr = curr.next
                prev = prev.next
        return head
