class Snake:
    def __init__(self, length, screen_height, screen_width, direction):
        self.length = length
        self.body = list()

        for x in range(self.length):
            self.body.append([screen_height // 2, screen_width // 2 - x])

        self.direction = direction
