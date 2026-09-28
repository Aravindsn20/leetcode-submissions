class Solution:
    def isPalindrome(self, s: str) -> bool:
        # rev = []
        # for cs in s:
        #     if ord('A') <= ord(cs) <= ord('Z') or ord('a') <= ord(cs) <= ord('z') or ord('0') <= ord(cs) <= ord('9'):
        #         rev.append(cs.lower())
        # return (rev == rev[::-1])
        

        # rev = []
        # for cs in s:
        #     if cs.isalnum():
        #         rev.append(cs.lower())
        # return (rev == rev[::-1])

        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

