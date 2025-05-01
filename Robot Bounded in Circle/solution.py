class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # north, east, south, west
        i = 0
        dirX, dirY = directions[i] # Start by facing north
        x, y = 0, 0 # current coords
        
        for instruction in instructions:
            if instruction == "G":
                x, y = x + dirX, y + dirY
            elif instruction == "L":    # Turn 90 degrees left
                i = (i - 1) % 4
                dirX, dirY = directions[i]
            else:                       # Turn 90 degrees right
                i = (i + 1) % 4
                dirX, dirY = directions[i]
        
        return (x, y) == (0, 0) or (dirX, dirY) != directions[0]