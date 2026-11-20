class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = res = max(piles)
        while r >= l:
            total = 0
            mid = (r + l) // 2
            for p in piles:
                total += math.ceil(p / mid)
            if total <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1 
        return res