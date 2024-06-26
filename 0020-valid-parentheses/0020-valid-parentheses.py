class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if len(stack) == 0 or (i == ')' and stack[-1] !='(') or (i == ']' and stack[-1] != '[') or (i == '}' and stack[-1] != '{'):
                    return False
                    break
                stack.pop()
        return len(stack) == 0