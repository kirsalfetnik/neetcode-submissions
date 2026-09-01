class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxProfit = 0

        while R < len(prices):
            if prices[R] > prices[L]:
                maxProfit += (prices[R] - prices[L])
                L = R
                R += 1
            else: 
                L = R
                R += 1
        
        return maxProfit
