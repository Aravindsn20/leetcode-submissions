class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search
        l = 1
        sumP = 0
        r = res = max(piles)
        while r >= l:
            sumP = 0
            mid = (l + r) // 2
            for p in piles:
                sumP +=  math.ceil(p / mid)
            if sumP > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
                
        return res