class DistanceSensor:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def scan_direction(self, position, direction):
        x, y = position
        dx, dy = direction
        distance = 0

        while True:
            x += dx
            y += dy
            distance += 1

            outside_grid = x < 0 or x >= self.width or y < 0 or y >= self.height

            if outside_grid:
                return distance - 1

            if (x, y) in self.obstacles:
                return distance

    def scan_all_directions(self, position):
        readings = {
            "right": self.scan_direction(position, (1, 0)),
            "left": self.scan_direction(position, (-1, 0)),
            "up": self.scan_direction(position, (0, 1)),
            "down": self.scan_direction(position, (0, -1)),
        }

        return readings
