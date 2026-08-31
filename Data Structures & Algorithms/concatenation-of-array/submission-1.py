class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans
        # Suggested Soln - 
        n = len(nums)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
        