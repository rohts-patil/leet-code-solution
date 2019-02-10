# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/603/


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
        nFromLast = head
        temp = head
        for i in range(n):
            nFromLast = nFromLast.next

        if not nFromLast:
            return head.next
        
        while nFromLast.next is not None:
            temp = temp.next
            nFromLast = nFromLast.next

        temp.next= temp.next.next

        return head