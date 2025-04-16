class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                product = int(num1[i1]) * int(num2[i2])

                res[i1 + i2] += product
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        # The res is in reverse currently, so reverse it to regular order
        res = res[::-1]

        # Strip the zero's from the start of the number
        i = 0
        while i < len(res):
            if res[i] == 0:
                i += 1
            else:
                break
        res = res[i:]

        for i in range(len(res)):
            res[i] = str(res[i])

        return "".join(res)