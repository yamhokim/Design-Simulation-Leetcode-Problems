class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: North, East, South, West
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_direction = 0

        obstacles = {tuple(obstacle) for obstacle in obstacles}
        curr_x, curr_y = 0, 0
        max_dist = 0

        for command in commands:
            if command == -2:
                curr_direction = (curr_direction - 1) % 4
            elif command == -1:
                curr_direction = (curr_direction + 1) % 4
            else:
                dx, dy = directions[curr_direction]
                for i in range(command):
                    if (curr_x + dx, curr_y + dy) in obstacles:
                        break
                    curr_x += dx
                    curr_y += dy
            curr_dist = curr_x**2 + curr_y**2
            max_dist = max(max_dist, curr_dist)
        
        return max_dist