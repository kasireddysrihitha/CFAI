# maze.py

class Maze:
    def __init__(self):
        # Maze Representation
        # 0 = Free Path
        # 1 = Wall
        # S = Start
        # G = Goal

        self.grid = [
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0]
        ]

        # Start Position
        self.start = (0, 0)

        # Goal Position
        self.goal = (4, 4)

    # Check if move is valid
    def is_valid_move(self, x, y):

        rows = len(self.grid)
        cols = len(self.grid[0])

        # Check boundaries
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return False

        # Check wall
        if self.grid[x][y] == 1:
            return False

        return True

    # Print Maze
    def print_maze(self):
        print("\nMaze Layout:")

        for i in range(len(self.grid)):
            row = ""

            for j in range(len(self.grid[0])):

                if (i, j) == self.start:
                    row += " S "

                elif (i, j) == self.goal:
                    row += " G "

                elif self.grid[i][j] == 1:
                    row += " # "

                else:
                    row += " . "

            print(row)