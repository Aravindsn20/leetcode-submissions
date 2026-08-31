class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for cs in s:
            if cs.isalnum():
                newstr += cs.lower()
        return newstr == newstr[::-1]
        