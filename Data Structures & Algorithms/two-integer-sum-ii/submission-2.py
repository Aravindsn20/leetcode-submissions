class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # My solution
        # Have  2 pointers - L, R
        # Condition - if val[l] + val[r] > target -> reduce r
        #             if val[l] + val[r] < target -> increase l  - > While l < r
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1        