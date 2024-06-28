class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        opened = 0
        for i in s:
            if i == '(' and opened > 0:
                stack.append(i)
            if i == ')' and opened > 1:
                stack.append(i)
            if i == '(':
                opened += 1
            else:
                opened -=1
        return "".join(stack)