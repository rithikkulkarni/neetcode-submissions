class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        s = s.lower()

        while l < r:
            if s[l].isalnum() and s[r].isalnum() and s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l].isalnum() and not s[r].isalnum():
                r -= 1
            elif not s[l].isalnum() and s[r].isalnum():
                l += 1
            elif not s[l].isalnum() and not s[r].isalnum():
                r -= 1
                l += 1
            else:
                return False
        return True