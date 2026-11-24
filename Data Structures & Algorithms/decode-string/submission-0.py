class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for cs in s:
            if cs != ']':
                stack.append(cs)
            else:
                substr = ''
                while stack[-1] != '[' and stack:
                    substr = stack.pop() + substr
                stack.pop() # pop the '['
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(num * substr)
        return "".join(stack)