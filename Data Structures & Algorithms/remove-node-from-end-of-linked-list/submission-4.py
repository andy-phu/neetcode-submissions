# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0 

        root = head 
        while root:
            counter += 1 
            root = root.next

        if counter == 1 and n == 1: 
            return None 


        dummy = ListNode()
        dummy.next = head 

        prev = dummy 
        current = head 

        targetIndex = counter - n 
        i = 0 

        while i < targetIndex: 
            prev = prev.next 
            current = current.next
            i += 1 
        print(i)
        prev.next = current.next

        return dummy.next 
            