class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Directions: right, down, left, up
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]

        res = []
        r, c = rStart, cStart
        direction = 0 # Start by moving right
        steps = 1

        while len(res) < rows * cols:
            for _ in range(2):
                dr, dc = directions[direction]
                for _ in range(steps):
                    if (0 <= r < rows and 0 <= c < cols):
                        res.append([r, c])
                    r, c = r + dr, c + dc
                direction = (direction + 1) % 4
            steps += 1

        return res