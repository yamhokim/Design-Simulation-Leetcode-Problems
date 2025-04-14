class Solution:
    def addDigits(self, num: int) -> int:
        global_sum = num

        while global_sum >= 10:
            local_sum = 0
            while global_sum > 0:
                local_sum += global_sum % 10
                global_sum //= 10
            
            global_sum = local_sum

        return global_sum