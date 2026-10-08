class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']

        stack = []

        for char in s:
            if char in opened:
                stack.append(char)
            elif char in closed and len(stack) == 0:
                return False
            elif char in closed and opened.index(stack[-1]) == closed.index(char):
                stack.pop()
            else:
                return False
        
        if len(stack) != 0:
            return False
        return True