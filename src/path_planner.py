import heapq


class AStarPlanner:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else set()

    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def get_neighbors(self, position):
        x, y = position

        possible_moves = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]

        valid_neighbors = []

        for move in possible_moves:
            new_x, new_y = move

            inside_grid = 0 <= new_x < self.width and 0 <= new_y < self.height
            not_obstacle = move not in self.obstacles

            if inside_grid and not_obstacle:
                valid_neighbors.append(move)

        return valid_neighbors

    def find_path(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score

                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return []

    def reconstruct_path(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()
        return path
