class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mdict = {}
        self.capacity = capacity
        self.left = Node(0, 0)       
        self.right = Node(0, 0)       
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if (key not in self.mdict):
            return -1
        node = self.mdict[key]
        self.remove(node)            
        self.insert(node)            
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.mdict:
            self.remove(self.mdict[key])  

        node = Node(key, value)
        self.mdict[key] = node
        self.insert(node)

        if len(self.mdict) > self.capacity:
            lru = self.left.next          
            self.remove(lru)
            del self.mdict[lru.key]       
        