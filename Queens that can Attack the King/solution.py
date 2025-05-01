class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        left, right = 0, 8
        top, bot = 0, 8
        queens = {(y, x) for y, x in queens}
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        res = []

        for direction in directions:
            dy, dx = direction
            curr_row, curr_col = king
            while top <= curr_row + dy < bot and left <= curr_col + dx < right:
                curr_row += dy
                curr_col += dx
                if (curr_row, curr_col) in queens:
                    res.append((curr_row, curr_col))
                    break
        
        return res