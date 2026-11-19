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
                if stack and stack[-1] == hashmap.get(cs):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cs)
        return not stack