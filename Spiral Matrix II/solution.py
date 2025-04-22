class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            row = [0] * n
            matrix.append(row)

        top = 0
        bottom = n
        left = 0
        right = n
        cur_val = 1

        while left < right and top < bottom:
            # Move right along the top border
            for col in range(left, right):
                matrix[top][col] = cur_val
                cur_val += 1
            
            # Update the top border
            top += 1

            # Move down along the right border
            for row in range(top, bottom):
                matrix[row][right-1] = cur_val
                cur_val += 1
            
            # Update the right border
            right -= 1

            # Move left along the bottom border
            for col in range(right - 1, left - 1, -1):
                matrix[bottom - 1][col] = cur_val
                cur_val += 1
            
            # Update the bottom border
            bottom -= 1

            # Move up along the left border
            for row in range(bottom - 1, top - 1, -1):
                matrix[row][left] = cur_val
                cur_val += 1
            
            # Update the left border
            left += 1

        return matrix

        