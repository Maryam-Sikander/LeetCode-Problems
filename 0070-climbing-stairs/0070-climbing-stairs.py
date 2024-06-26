class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n==1:
            return 1
        x = 1
        y = 1
        for i in range(2, n + 1):
            next_term = x + y
            x = y
            y = next_term
        return next_term