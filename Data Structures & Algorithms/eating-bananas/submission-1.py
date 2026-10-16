class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValidK(k):
            return sum(math.ceil(p / k) for p in piles) <= h

        total = 0
        maxPile = 0
        for p in piles:
            total += p
            if p > maxPile:
                maxPile = p
        l = math.ceil(total / h)
        r = maxPile

        lowestK = r + 1

        while l <= r:
            m = (r + l) // 2
            if isValidK(m):
                lowestK = m
                r = m - 1
            else:
                l = m + 1
            
        return lowestK
