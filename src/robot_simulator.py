import matplotlib.pyplot as plt


class RobotSimulator:
    def __init__(self, start_x=0, start_y=0):
        self.x = start_x
        self.y = start_y
        self.path = [(self.x, self.y)]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.path.append((self.x, self.y))

    def plot_path(self):
        x_values = [point[0] for point in self.path]
        y_values = [point[1] for point in self.path]

        plt.figure()
        plt.plot(x_values, y_values, marker="o")
        plt.title("Basic Robot Movement Simulation")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    robot = RobotSimulator()

    robot.move(1, 0)
    robot.move(1, 1)
    robot.move(0, 1)
    robot.move(-1, 0)

    robot.plot_path()
