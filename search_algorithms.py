from collections import deque
import heapq


class SearchAlgorithms:

    # -------------------------
    # BFS
    # -------------------------
    def bfs(self, maze):

        queue = deque()
        queue.append((maze.start, [maze.start]))

        visited = set()
        visited.add(maze.start)

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while queue:

            current, path = queue.popleft()

            if current == maze.goal:
                return path

            x, y = current

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if maze.is_valid_move(nx, ny):

                    next_cell = (nx, ny)

                    if next_cell not in visited:

                        visited.add(next_cell)

                        queue.append(
                            (
                                next_cell,
                                path + [next_cell]
                            )
                        )

        return None

    # -------------------------
    # DFS
    # -------------------------
    def dfs(self, maze):

        stack = []
        stack.append((maze.start, [maze.start]))

        visited = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while stack:

            current, path = stack.pop()

            if current == maze.goal:
                return path

            if current not in visited:

                visited.add(current)

                x, y = current

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    if maze.is_valid_move(nx, ny):

                        next_cell = (nx, ny)

                        if next_cell not in visited:

                            stack.append(
                                (
                                    next_cell,
                                    path + [next_cell]
                                )
                            )

        return None

    # -------------------------
    # UCS
    # -------------------------
    def ucs(self, maze):

        pq = []
        heapq.heappush(
            pq,
            (0, maze.start, [maze.start])
        )

        visited = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while pq:

            cost, current, path = heapq.heappop(pq)

            if current == maze.goal:
                return path, cost

            if current not in visited:

                visited.add(current)

                x, y = current

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    if maze.is_valid_move(nx, ny):

                        next_cell = (nx, ny)

                        if next_cell not in visited:

                            heapq.heappush(
                                pq,
                                (
                                    cost + 1,
                                    next_cell,
                                    path + [next_cell]
                                )
                            )

        return None, 0

    # -------------------------
    # Heuristic Function
    # -------------------------
    def heuristic(self, current, goal):

        x1, y1 = current
        x2, y2 = goal

        return abs(x1 - x2) + abs(y1 - y2)

    # -------------------------
    # A* Search
    # -------------------------
    def astar(self, maze):

        pq = []

        heapq.heappush(
            pq,
            (
                0,
                maze.start,
                [maze.start],
                0
            )
        )

        visited = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while pq:

            total_cost, current, path, cost = (
                heapq.heappop(pq)
            )

            if current == maze.goal:
                return path, cost

            if current not in visited:

                visited.add(current)

                x, y = current

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    if maze.is_valid_move(nx, ny):

                        next_cell = (nx, ny)

                        if next_cell not in visited:

                            new_cost = cost + 1

                            h_cost = self.heuristic(
                                next_cell,
                                maze.goal
                            )

                            total = (
                                new_cost + h_cost
                            )

                            heapq.heappush(
                                pq,
                                (
                                    total,
                                    next_cell,
                                    path + [next_cell],
                                    new_cost
                                )
                            )

        return None, 0