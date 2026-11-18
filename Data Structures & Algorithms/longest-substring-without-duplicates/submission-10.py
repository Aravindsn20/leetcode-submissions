class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charset = set()
        # l, r = 0, 1
        # res = 1
        # if not s:
        #     return 0
        # charset.add(s[l])
        # for r in range(1, len(s)):
        #     while s[r] in charset:
        #         charset.remove(s[l])
        #         l += 1
        #     charset.add(s[r])
        #     res = max(res, r - l + 1)
        # return res

        l, max_Window = 0, 0
        charset = set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_Window = max(max_Window, r - l + 1)
        return max_Window