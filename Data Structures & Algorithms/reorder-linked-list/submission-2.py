# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        
        [2,4,6,8]
               f
           s
        
        
        [2,4,6,8,10]
        s
             f
        """

        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None 
        slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            

        first = head
        second = prev

        while second:
            temp_first = first.next
            temp_second = second.next

            first.next = second 
            second.next = temp_first

            second = temp_second
            first = temp_first

         
        
        
            


