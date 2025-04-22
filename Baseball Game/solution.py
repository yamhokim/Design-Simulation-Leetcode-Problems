'''
Initial Approach
'''
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for operation in operations:
            if operation == '+':
                res.append(res[-1] + res[-2])
            elif operation == 'D':
                res.append(res[-1] * 2)
            elif operation == 'C':
                res = res[:-1]
            else:
                res.append(int(operation))

        return sum(res)


'''
Approach Using a Stack
'''
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == "C":
                if record:
                    record.pop() # last item in stack is now not valid
            elif operation == "+":
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])
            elif operation == "D":
                if record:
                    record.append(record[-1] * 2)
            else:
                record.append(int(operation))
        return sum(record)