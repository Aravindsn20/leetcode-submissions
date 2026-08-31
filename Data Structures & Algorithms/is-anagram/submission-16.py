class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Approach 1 - Sort & compare
        sorted_S = "".join(sorted(s))
        sorted_T = "".join(sorted(t))
        if sorted_S == sorted_T:
            return True
        else:
            return False
