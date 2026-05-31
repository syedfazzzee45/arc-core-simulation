from src.path_planner import AStarPlanner
from src.sensors import DistanceSensor


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

    sensor = DistanceSensor(width, height, obstacles)

    print("Navigation with Sensor Readings")
    print("--------------------------------")
    print("Start:", start)
    print("Goal:", goal)
    print("Planned path:", path)
    print()

    for step_number, position in enumerate(path):
        readings = sensor.scan_all_directions(position)

        print(f"Step {step_number}: Robot at {position}")
        print("Sensor readings:")
        print(f"  Right: {readings['right']}")
        print(f"  Left: {readings['left']}")
        print(f"  Up: {readings['up']}")
        print(f"  Down: {readings['down']}")
        print()


if __name__ == "__main__":
    main()
