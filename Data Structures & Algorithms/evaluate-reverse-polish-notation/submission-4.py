class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}

        for item in tokens:
            if not item in operands:
                stack.append(int(item))
            else:
                second = stack.pop()
                first = stack.pop()
                if item == '+':
                    result = first + second
                elif item == '-':
                    result = first - second
                elif item == '*':
                    result = first * second
                else:
                    result = int(first / second)
                
                stack.append(result)
        return stack[-1]
            