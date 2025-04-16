class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0 
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        while left < right and top < bottom:
            # Start moving right (along the top row)
            for col in range(left, right):
                res.append(matrix[top][col])
            top += 1

            # Start moving down (along the right col)
            for row in range(top, bottom):
                res.append(matrix[row][right - 1])
            right -= 1

            # Check if the statement still holds
            if not (left < right and top < bottom):
                break

            # Start moving left (along the bottom row)
            for col in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][col])
            bottom -= 1

            # Start moving up (along the left col)
            for row in range(bottom - 1, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res