# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        curr1 = l1
        curr2 = l2
        ret_curr = None
        ret_head = None
        while curr1 and curr2:
            val = curr1.val + curr2.val
            if carry:
                val += 1

            if not ret_head:
                ret_head = ListNode(val)
                ret_curr = ret_head
            else:
                ret_curr.next = ListNode(val)
                ret_curr = ret_curr.next

            if val >= 10:
                ret_curr.val -= 10
                carry = True
            else:
                carry = False
            curr1 = curr1.next
            curr2 = curr2.next

        if curr1:
            ret_curr.next = curr1
        elif curr2:
            ret_curr.next = curr2

        if carry:
            if ret_curr.next:
                ret_curr = ret_curr.next
                ret_curr.val += 1
            else:
                ret_curr.next = ListNode(1)
                ret_curr = ret_curr.next
            while ret_curr and ret_curr.val >= 10:
                ret_curr.val -= 10
                if ret_curr.next:
                    ret_curr.next.val += 1
                else:
                    ret_curr.next = ListNode(1)
                ret_curr = ret_curr.next

        return ret_head
