class Solution:
    def isPalindrome(self, s: str) -> bool:
        # rev = []
        # for cs in s:
        #     if ord('A') <= ord(cs) <= ord('Z') or ord('a') <= ord(cs) <= ord('z') or ord('0') <= ord(cs) <= ord('9'):
        #         rev.append(cs.lower())
        # return (rev == rev[::-1])
        rev = []
        for cs in s:
            if cs.isalnum():
                rev.append(cs.lower())
        return (rev == rev[::-1])