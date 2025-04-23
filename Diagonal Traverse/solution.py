class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])

        res = []
        cur_row = 0
        cur_col = 0

        going_up = True

        while len(res) != ROWS * COLS:
            if going_up:
                while cur_row >= 0 and cur_col < COLS:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                
                # Reset the position back within the bound
                # Case 1: cur_col == COLS
                if cur_col == COLS:
                    cur_row += 2
                    cur_col -= 1
                # Case 2: cur_col < COLS
                else:
                    cur_row += 1
                
                # Change the direction of travel
                going_up = False
            else:
                while cur_row < ROWS and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                
                # Reset the position back within the bounds
                # Case 1: cur_row == ROWS
                if cur_row == ROWS:
                    cur_row -= 1
                    cur_col += 2
                # Case 2: cur_row < ROWS
                else:
                    cur_col += 1

                # Switch the direction of travel
                going_up = True
            
        return res