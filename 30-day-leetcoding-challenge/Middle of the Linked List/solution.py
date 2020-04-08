### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        while fast != None:
            
            if fast.next == None:
                return slow
            
            else:
                slow = slow.next
                fast = fast.next
                fast = fast.next
                
        return slow    