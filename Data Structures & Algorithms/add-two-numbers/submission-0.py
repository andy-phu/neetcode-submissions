# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #traverse both linked lists and put them into strings 
        #reverse the strings and conver them to integers 
        #add the two new ints and convert the sum to a string 
        #from the string reverse it and traverse creating a new linked list 

        string_1 = ""
        string_2 = ""

        while l1:
            string_1 += str(l1.val)
            l1 =  l1.next

        while l2:
            string_2 += str(l2.val)
            l2 =  l2.next

        int_1 = int(string_1[::-1])
        int_2 =  int(string_2[::-1])

        total = str(int_1 + int_2)

        total = total[::-1]
        head = curr = ListNode(0)

        for t in total:
            curr.next = ListNode(int(t))
            curr = curr.next

        return head.next

        



