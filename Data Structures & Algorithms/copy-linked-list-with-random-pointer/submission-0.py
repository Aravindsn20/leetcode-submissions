class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None : None} # To track the pointers of the original LL
        temp = head

        while temp:
            # Add original node and its copy to the hashmap
            newnode = Node(temp.val)
            hashmap[temp] = newnode
            temp = temp.next

        temp = head
        while temp:
            hashmap[temp].next = hashmap[temp.next]
            hashmap[temp].random = hashmap[temp.random]
            temp = temp.next
        
        return hashmap[head] 
