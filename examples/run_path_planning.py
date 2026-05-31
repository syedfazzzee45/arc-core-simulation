import matplotlib.pyplot as plt

from src.path_planner import AStarPlanner


def plot_path(width, height, obstacles, path, start, goal):
    plt.figure()

    for x in range(width):
        for y in range(height):
            plt.scatter(x, y, marker="s", alpha=0.2)

    for obstacle in obstacles:
        plt.scatter(obstacle[0], obstacle[1], marker="X", s=200, label="Obstacle")

    if path:
        path_x = [point[0] for point in path]
        path_y = [point[1] for point in path]
        plt.plot(path_x, path_y, marker="o", label="Planned Path")

    plt.scatter(start[0], start[1], marker="o", s=200, label="Start")
    plt.scatter(goal[0], goal[1], marker="*", s=250, label="Goal")

    plt.title("A* Path Planning Simulation")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.xlim(-1, width)
    plt.ylim(-1, height)
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    width = 10
    height = 10

    obstacles = {
        (2, 2),
        (2, 3),
        (2, 4),
        (3, 4),
        (4, 4),
        (5, 4),
    }

    start = (0, 0)
    goal = (8, 8)

    planner = AStarPlanner(width, height, obstacles)
    path = planner.find_path(start, goal)

    print("Planned path:")
    print(path)

    plot_path(width, height, obstacles, path, start, goal)


if __name__ == "__main__":
    main()
