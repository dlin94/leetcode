# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == headB:
            return headA
        elif headA == None or headB == None:
            return None

        fastA = headA
        lenA = 1
        fastB = headB
        lenB = 1
        breakA = False
        breakB = False
        while True:
            print(fastA.val, lenA)
            print(fastB.val, lenB)
            if not breakA:
                if not fastA.next and not breakA:
                    breakA = True
                elif not fastA.next.next and not breakA:
                    lenA += 1
                    breakA = True
                else:
                    fastA = fastA.next.next
                    lenA += 2

            if not breakB:
                if not fastB.next:
                    breakB = True
                elif not fastB.next.next:
                    lenB += 1
                    breakB = True
                else:
                    fastB = fastB.next.next
                    lenB += 2


            #if (not fastA.next or not fastA.next.next) and (not fastB.next or not fastB.next.next):
            if breakA and breakB:
                break

        print("start")
        print(lenA, lenB)
        print(headA.val, headB.val)
        if lenA > lenB:
            diff = lenA - lenB
            for i in range(0, diff):
                headA = headA.next
        else:
            diff = lenB - lenA
            for i in range(0, diff):
                headB = headB.next

        print(headA.val, headB.val)
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
