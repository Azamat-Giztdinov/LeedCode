class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0
        for i in prices:
            minPrice = min(i, minPrice)
            maxPrice = max(maxPrice, i-minPrice)
        return maxPrice