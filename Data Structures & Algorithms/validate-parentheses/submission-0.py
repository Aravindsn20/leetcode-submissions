class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for cs in s:
            if cs in hashmap:
                if stack and stack[-1] == hashmap[cs]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(cs)
        return len(stack) == 0
