import matplotlib.pyplot as plt


class GridWorld:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.robot_position = [0, 0]
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def move_robot(self, dx, dy):
        new_x = self.robot_position[0] + dx
        new_y = self.robot_position[1] + dy

        if not self._is_inside_grid(new_x, new_y):
            print("Move blocked: outside grid")
            return

        if (new_x, new_y) in self.obstacles:
            print("Move blocked: obstacle detected")
            return

        self.robot_position = [new_x, new_y]

    def _is_inside_grid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def plot_world(self):
        plt.figure()

        for x in range(self.width):
            for y in range(self.height):
                plt.scatter(x, y, marker="s", alpha=0.2)

        for obstacle in self.obstacles:
            plt.scatter(obstacle[0], obstacle[1], marker="X", s=200, label="Obstacle")

        plt.scatter(
            self.robot_position[0],
            self.robot_position[1],
            marker="o",
            s=200,
            label="Robot",
        )

        plt.title("Grid World Robot Simulation")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.xlim(-1, self.width)
        plt.ylim(-1, self.height)
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    world = GridWorld()

    world.add_obstacle(2, 2)
    world.add_obstacle(3, 3)

    world.move_robot(1, 0)
    world.move_robot(1, 0)
    world.move_robot(0, 1)

    world.plot_world()
