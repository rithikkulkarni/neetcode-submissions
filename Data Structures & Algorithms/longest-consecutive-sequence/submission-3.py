class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            hashset.add(n)

        maxLength = 0
        currLength = 0
        
        for n in nums:
            currLength = 0
            if n-1 not in hashset:
                value = n
                while value in hashset:
                    value += 1
                    currLength += 1
                maxLength = max(currLength, maxLength)
        
        return maxLength