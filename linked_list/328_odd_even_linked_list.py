# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        even_start = even

        while True:
            odd.next = odd.next.next # link odd to odd
            odd = odd.next # odd is now the next odd
            even.next = even.next.next # link even to even
            even = even.next

            if not odd.next or not even.next:
                odd.next = even_start
                break
            #elif not even.next:
            #    odd.next =
        return head
