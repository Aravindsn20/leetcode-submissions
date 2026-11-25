# Capacity 

# When PUT -> Cehck the hashmap, if in hasmap, then update the code in the DLL, if NOT, check the capacity, if withing capcaity, then create the node, add it next to head. if not within capacity, remove node near tail, add the new node next to head

# Get -> check the hashmap, if in hashmap, then return the value(node).val. if not return -1.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        #establishing link - 
        self.head.right = self.tail
        self.tail.left = self.head
    
    def insert(self, node):
        temp = self.head.right
        temp.left = node
        self.head.right = node
        node.right = temp
        node.left = self.head

    def delete(self, node):
        tempR = node.right
        tempL = node.left

        tempL.right = tempR
        tempR.left = tempL

    def get(self, key):
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]

        self.delete(node)
        self.insert(node)

        return self.hashmap[key].val

    def put(self, key, val):
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = val

            self.delete(node)
            self.insert(node)

        else:
            if len(self.hashmap) == self.capacity:
                nodeLRU = self.tail.left 

                self.delete(nodeLRU)
                del self.hashmap[nodeLRU.key]
                
                node = Node(key, val)
                self.insert(node)

                self.hashmap[node.key] = node 
            
            else:
                node = Node(key, val)
                self.insert(node)
                
                self.hashmap[node.key] = node


# LRU Cache
cache = LRUCache(2)

# Queries
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")
cache.put(3, 3)
print(cache.get(2), end=" ")
cache.put(4, 4)
print(cache.get(1), end=" ")
print(cache.get(3), end=" ")
print(cache.get(4), end=" ")