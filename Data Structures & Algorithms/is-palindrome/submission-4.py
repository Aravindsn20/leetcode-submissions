class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newstr = ''
        # for cs in s:
        #     if cs.isalnum():
        #         newstr += cs.lower()
        # return newstr == newstr[::-1]

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isalnumcheck(s[l]):
                l += 1
            while l < r and not self.isalnumcheck(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isalnumcheck(self, s):
        return(
            ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9')
        )
                