class Robot:

    def __init__(self, width: int, height: int):
        self.curr_step = 0
        self.pos = [((0, 0), "South")]
        for i in range(1, width):
            self.pos.append(((i, 0), "East"))
        for j in range(1, height):
            self.pos.append(((width - 1, j), "North"))
        for k in range(width - 2, -1, -1):
            self.pos.append(((k, height - 1), "West"))
        for l in range(height - 2, 0, -1):
            self.pos.append(((0, l), "South"))
        self.isOrigin = True

    def step(self, num: int) -> None:
        self.isOrigin = False
        self.curr_step = (self.curr_step + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return self.pos[self.curr_step][0]

    def getDir(self) -> str:
        return "East" if self.isOrigin else self.pos[self.curr_step][1]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()