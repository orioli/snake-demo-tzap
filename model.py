class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0][0], self.body[0][1]
        if self.direction == "RIGHT":
            x += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
            
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        # Prevent the snake from turning back on itself
        if new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction