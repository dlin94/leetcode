# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return

        head, head.next = ListNode(0), head
        #p = head
        #n = head.next
        slow = head
        fast = head
        length = 0
        slow_position = 0
        while True:
            if not fast.next:
                break
            elif not fast.next.next:
                length += 1
                break
            else:
                slow = slow.next
                fast = fast.next.next
                slow_position += 1
                length += 2
        if length - n + 1 > slow_position:
            curr = slow
            curr_position = slow_position
        else:
            curr = head
            curr_position = 0

        while curr_position <= length - n + 1:
            print(curr.val, curr_position)
            if curr_position == length - n:
                curr.next = curr.next.next
                break
            curr = curr.next
            curr_position += 1

        return head.next
