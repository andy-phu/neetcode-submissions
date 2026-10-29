# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #for middle 
        #for beginning 

        #count the size first 

        curr = head 
        size = 0
        while curr:
            size += 1
            curr = curr.next

        #beginning
        if n == size:
            return head.next
        
        diff = size - n 
        curr = head 
        i = 0 
        for i in range(diff-1):
            curr = curr.next 

        print(curr.val)
        curr.next = curr.next.next

        return head
