"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #have a set that contains all the indexes that are created 
        #if the random val is not in the set, then create a new node 

        curr = head 

        linked_map = {None:None}

        while curr:
            copy = Node(curr.val)
            linked_map[curr] = copy
            curr = curr.next

        #linked list now has the old nodes pointing to the new node without the next and random 


        curr = head 
        #connect the next and random 
        while curr:
            linked_map[curr].next = linked_map[curr.next]
            linked_map[curr].random = linked_map[curr.random]
            curr = curr.next

        return linked_map[head]

