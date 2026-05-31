from src.grid_world import GridWorld


def main():
    world = GridWorld(width=10, height=10)

    world.add_obstacle(2, 2)
    world.add_obstacle(3, 3)
    world.add_obstacle(4, 4)

    movements = [
        (1, 0),
        (1, 0),
        (0, 1),
        (0, 1),
        (1, 0),
    ]

    for dx, dy in movements:
        world.move_robot(dx, dy)

    world.plot_world()


if __name__ == "__main__":
    main()
