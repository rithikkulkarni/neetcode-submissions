class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSell = 0
        minPrice = float('inf')

        for p in prices:
            if p - minPrice > maxSell:
                maxSell = p - minPrice
            if p < minPrice:
                minPrice = p
        
        return maxSell