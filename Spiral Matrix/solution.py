class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        while top < bottom and left < right:
            # Move right along the top boundary
            for col in range(left, right):
                res.append(matrix[top][col])

            # Update the top boundary
            top += 1

            # Move down along the right boundary
            for row in range(top, bottom):
                res.append(matrix[row][right-1])

            # Update the right boundary
            right -= 1

            # Perform intermediate check of the condition
            if not (top < bottom and left < right):
                break

            # Move left along the bottom boundary
            for col in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][col])

            # Update the bottom boundary
            bottom -= 1

            # Move up along the left boundary
            for row in range(bottom - 1, top - 1, -1):
                res.append(matrix[row][left])

            # Update the left boundary
            left += 1
            
        return res