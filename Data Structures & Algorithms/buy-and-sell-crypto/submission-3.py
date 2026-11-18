class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low and sell high, 2 pointer approach. 
        l = maxP = profit = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
            maxP = max(maxP, profit) 
        return maxP 