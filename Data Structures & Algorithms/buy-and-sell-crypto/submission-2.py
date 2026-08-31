class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        bestProfit = 0

        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
                R += 1
            else:
                bestProfit = max(bestProfit, prices[R] - prices[L])
                R += 1

        return bestProfit 