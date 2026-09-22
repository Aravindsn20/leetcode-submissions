class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_N = sorted(set(nums))

        if not sorted_N:
            return 0

        l = 1
        curr = 1

        for i in range(1, len(sorted_N)):
            if sorted_N[i] == sorted_N[i - 1] + 1:
                curr += 1
            else:
                l = max(l, curr)
                curr = 1

        return max(l, curr)