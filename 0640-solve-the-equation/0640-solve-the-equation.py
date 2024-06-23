import re
def solve(sides):
        term = re.findall(r'[+-]?\d*x?', sides.replace(' ', ''))
        var_x = 0
        constant = 0
        for t in term:
            if 'x' in t:
                if t == 'x' or t == '+x':
                    var_x += 1
                elif t == '-x':
                    var_x -= 1
                else:
                    var_x += int(t.replace('x', ''))
            else:
                if t:
                    constant += int(t)
        return var_x, constant
class Solution:
    
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split('=')
        left_var, left_constant = solve(l)
        right_var, right_constant = solve(r)
        # calculate variables and constants
        x_var = left_var - right_var
        x_constant = right_constant - left_constant 

        if x_var == 0:
            if x_constant == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'

        x_value = x_constant / x_var
        if x_value.is_integer():
            return f'x={int(x_value)}'
        else:
            return "No solution"

        