class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)
        sequence_starters = []
        for n in nums:
            if n - 1 not in hashset:
                sequence_starters.append(n)
        
        max_length = 1
        curr_length = 1
        for n in sequence_starters:
            k = n + 1
            while k in hashset:
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
                k += 1
            else:
                curr_length = 1
        
        return max_length
            