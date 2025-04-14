class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        a_index = len(a) - 1
        b_index = len(b) - 1
        carry = 0

        while a_index >= 0 or b_index >= 0 or carry:
            a_val = 0 if a_index < 0 else int(a[a_index])
            b_val = 0 if b_index < 0 else int(b[b_index])

            res.append(str(a_val ^ b_val ^ carry))
            carry = a_val & b_val or a_val & carry or b_val & carry
            a_index -= 1
            b_index -= 1
        
        return "".join(res[::-1])