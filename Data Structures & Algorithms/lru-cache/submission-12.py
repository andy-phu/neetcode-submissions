class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict()
        self.cap = capacity

        self.LRU = Node(-1, -1, None, None)
        self.MRU = Node(-1, -1, None, None)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def add(self, node):
        prev_MRU_node = self.MRU.prev

        node.prev = self.MRU.prev
        node.next = self.MRU

        prev_MRU_node.next = node
        self.MRU.prev = node


    def delete(self, key):
        node = self.map[key]
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode 
        return

    def get(self, key: int) -> int:
        if key in self.map:
            self.delete(key)
            self.add(self.map[key])
            return self.map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #delete the current node and bring it to the back
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.delete(key)
            self.add(node)
        else:
            node = Node(key, value, self.MRU.prev, self.MRU)
            self.map[key] = node 
            self.add(node)
        
        if len(self.map) > self.cap:
            target_node = self.LRU.next
            
            target_key = target_node.key
            
            self.delete(target_key)
            del self.map[target_key]



        