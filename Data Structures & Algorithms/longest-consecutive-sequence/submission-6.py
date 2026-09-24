class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        long = 0
        for n in nums:
            if n-1 not in nums:
                length = 1
                while (n + 1) in nums:
                    length += 1
                    n += 1
                long = max(length, long)
        return long