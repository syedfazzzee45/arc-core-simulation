from src.sensors import DistanceSensor


def main():
    width = 10
    height = 10

    obstacles = {
        (4, 2),
        (2, 5),
        (7, 7),
    }

    robot_position = (2, 2)

    sensor = DistanceSensor(width, height, obstacles)
    readings = sensor.scan_all_directions(robot_position)

    print("Robot position:", robot_position)
    print("Sensor readings:")

    for direction, distance in readings.items():
        print(f"{direction}: {distance}")


if __name__ == "__main__":
    main()
