class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min is 1, max can be max(piles)
        l = 1
        r = max(piles) - 1
        res = max(piles)
        while l <= r:
            mid = (l + r) // 2
            sumP = 0
            for p in piles:
                sumP += math.ceil(p / mid)
            if sumP > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res
