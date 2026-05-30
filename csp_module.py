# csp_module.py


class CSPModule:

    def __init__(self):
        pass

    # Check constraints
    def is_valid(self, maze, x, y, visited):

        # Stay inside maze
        if not maze.is_valid_move(x, y):
            return False

        # Avoid revisiting same cell
        if (x, y) in visited:
            return False

        return True

    # Backtracking Search
    def backtracking_search(self, maze):

        start = maze.start
        goal = maze.goal

        visited = set()

        path = []

        if self.solve(
                maze,
                start[0],
                start[1],
                goal,
                visited,
                path
        ):
            return path

        return None

    # Recursive solving
    def solve(
            self,
            maze,
            x,
            y,
            goal,
            visited,
            path
    ):

        # Check constraints
        if not self.is_valid(
                maze,
                x,
                y,
                visited
        ):
            return False

        # Add current cell
        visited.add((x, y))
        path.append((x, y))

        # Goal reached
        if (x, y) == goal:
            return True

        # Directions
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        # Try all possible paths
        for dx, dy in directions:

            new_x = x + dx
            new_y = y + dy

            if self.solve(
                    maze,
                    new_x,
                    new_y,
                    goal,
                    visited,
                    path
            ):
                return True

        # Backtracking
        path.pop()

        return False