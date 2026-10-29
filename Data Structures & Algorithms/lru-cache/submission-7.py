class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.LRU = Node(-1,-1, None, None)
        self.MRU = Node(-1, -1, None, None)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    
    def remove(self, node):
        leftNode = node.prev
        rightNode = node.next

        leftNode.next = rightNode
        rightNode.prev = leftNode

    def insert(self, node):
        tempNode = self.MRU.prev
        node.prev = tempNode
        tempNode.next = node

        self.MRU.prev = node
        node.next = self.MRU


    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        #if get is used move the node to the end before the mru node


    def put(self, key: int, value: int) -> None:
        #both scenarios
        #put in the linked list before the mru making the new node the mru

        #doesnt exist yet
        #put in the cache
        if key not in self.cache:
            #make node
            node = Node(key, value, None, None)
            self.cache[key] = node
            #key already exists
            #update the cache value 
            self.insert(node)

            #if the size is now greater than the capacity then point the lru to the next node and remove the value key,val from the cache
            if len(self.cache) > self.size:
                #remove key,val from cache
                del self.cache[self.LRU.next.key]
                self.remove(self.LRU.next)
        else: 
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])



    

        
