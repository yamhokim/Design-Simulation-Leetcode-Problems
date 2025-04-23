class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0:
            return False

        horizontal = 0
        vertical = 0

        for i in range(len(moves)):
            if moves[i] == 'R':
                horizontal += 1
            elif moves[i] == 'L':
                horizontal -= 1
            elif moves[i] == 'U':
                vertical += 1
            elif moves[i] == 'D':
                vertical -= 1
        
        return horizontal == 0 and vertical == 0