class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])

            maxLength = max(r - l + 1, maxLength)
            
        return maxLength