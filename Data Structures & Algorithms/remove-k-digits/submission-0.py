class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        res = ''
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                k -= 1
                stack.pop()
            stack.append(n)
        if k > 0:
            stack = stack[:len(stack) - k]
        res = ''.join(stack).lstrip('0')
        if res:
            return res
        else:
            return "0"
 