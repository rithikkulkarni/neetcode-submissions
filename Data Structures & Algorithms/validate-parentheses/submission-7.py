class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ")" : "(", "]" : "[", "}" : "{" }

        stack = []

        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap and len(stack) == 0:
                return False
            elif char in hashmap and hashmap[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0