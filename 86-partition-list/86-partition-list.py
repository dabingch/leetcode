# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        p1, p2, p = dummy1, dummy2, head
        
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            
            temp = p.next
            p.next = None
            p = temp
        
        p1.next = dummy2.next
        return dummy1.next
            