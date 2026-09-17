class Solution:
    # My Soln without rferring - 
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            numlen = ''
            while s[i] != '#':
                numlen += s[i]
                i += 1
            res.append(s[i + 1 : i + int(numlen) + 1])
            i = i + int(numlen) + 1
        return res
