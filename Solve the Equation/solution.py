class Solution:
    def solveEquation(self, equation: str) -> str:
        equal_index = equation.find('=')
        left_exp = equation[:equal_index]
        right_exp = equation[equal_index+1:]

        if left_exp[0] != '-':
            left_exp = '+' + left_exp
        if right_exp[0] != '-':
            right_exp = '+' + right_exp

        left = 0
        right = 0

        # Iterate over the left expression
        i = 0
        while i < len(left_exp):
            sign = 1 if left_exp[i] == '+' else -1
            i += 1
            val = ''
            while i < len(left_exp) and left_exp[i] not in ['+',  '-']:
                val += left_exp[i]
                i += 1
            
            if val[-1] == 'x':
                coeff = val[:-1]
                left += int(coeff) * sign if len(val) > 1 else 1 * sign
            else:
                right -= int(val) * sign
            
        # Iterate over the right expression
        j = 0
        while j < len(right_exp):
            sign = 1 if right_exp[j] == '+' else -1
            j += 1
            val = ''
            while j < len(right_exp) and right_exp[j] not in ['+', '-']:
                val += right_exp[j]
                j += 1

            if val[-1] == 'x':
                coeff = val[:-1]
                left -= int(coeff) * sign if len(val) > 1 else 1 * sign
            else:
                right += int(val) * sign

        # Compare the left and right sums
        if left == 0 and right == 0:
            return "Infinite solutions"
        elif left == 0:
            return "No solution"
        else:
            res = int(right / left)
            return f"x={res}"