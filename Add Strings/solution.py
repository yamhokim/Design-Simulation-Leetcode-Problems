class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        num1_index = len(num1) - 1
        num2_index = len(num2) - 1
        carry = 0
        
        while num1_index >= 0 or num2_index >= 0 or carry:
            num1_digit = 0 if num1_index < 0 else ord(num1[num1_index]) - ord("0")
            num2_digit = 0 if num2_index < 0 else ord(num2[num2_index]) - ord("0")
            digit_sum = num1_digit + num2_digit + carry
            carry = 1 if digit_sum >= 10 else 0
            res.append(str(digit_sum - 10 if digit_sum >= 10 else digit_sum))

            num1_index -= 1
            num2_index -= 1
        
        return "".join(res[::-1])