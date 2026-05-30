# gui_visualization.py

import tkinter as tk


class MazeGUI:

    def __init__(self, maze, path=None):

        self.maze = maze
        self.path = path

        self.cell_size = 60

        rows = len(maze.grid)
        cols = len(maze.grid[0])

        self.window = tk.Tk()
        self.window.title("AI Maze Solver Visualization")

        self.canvas = tk.Canvas(
            self.window,
            width=cols * self.cell_size,
            height=rows * self.cell_size
        )

        self.canvas.pack()

        self.draw_maze()

        self.window.mainloop()

    def draw_maze(self):

        rows = len(self.maze.grid)
        cols = len(self.maze.grid[0])

        for i in range(rows):
            for j in range(cols):

                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = "white"

                # Wall
                if self.maze.grid[i][j] == 1:
                    color = "black"

                # Path
                if self.path and (i, j) in self.path:
                    color = "light blue"

                # Start
                if (i, j) == self.maze.start:
                    color = "green"

                # Goal
                if (i, j) == self.maze.goal:
                    color = "red"

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="gray"
                )

                # Coordinates text
                self.canvas.create_text(
                    x1 + 30,
                    y1 + 30,
                    text=f"{i},{j}"
                )