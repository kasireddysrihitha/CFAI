# main.py

from maze import Maze
from search_algorithms import SearchAlgorithms
from csp_module import CSPModule
from decision_agent import DecisionAgent
from uncertainty import UncertaintyHandler
from gui_visualization import MazeGUI

# Create Maze Object
maze = Maze()

# Print Maze
maze.print_maze()

# Create Search Object
search = SearchAlgorithms()


# -----------------------
# BFS
# -----------------------
print("\n----- BFS Search -----")

bfs_path = search.bfs(maze)

if bfs_path:
    print("BFS Path Found:")
    print(bfs_path)
    print("Steps:", len(bfs_path) - 1)
else:
    print("No path found")


# -----------------------
# DFS
# -----------------------
print("\n----- DFS Search -----")

dfs_path = search.dfs(maze)

if dfs_path:
    print("DFS Path Found:")
    print(dfs_path)
    print("Steps:", len(dfs_path) - 1)
else:
    print("No path found")


# -----------------------
# UCS
# -----------------------
print("\n----- UCS Search -----")

ucs_path, ucs_cost = search.ucs(maze)

if ucs_path:
    print("UCS Path Found:")
    print(ucs_path)
    print("Cost:", ucs_cost)
    print("Steps:", len(ucs_path) - 1)
else:
    print("No path found")


# -----------------------
# A* Search
# -----------------------
print("\n----- A* Search -----")

astar_path, astar_cost = search.astar(maze)

if astar_path:
    print("A* Path Found:")
    print(astar_path)
    print("Cost:", astar_cost)
    print("Steps:", len(astar_path) - 1)
else:
    print("No path found")
 # -----------------------
# CSP Module
# -----------------------

print("\n----- CSP Backtracking Search -----")

csp = CSPModule()

csp_path = csp.backtracking_search(maze)

if csp_path:
    print("CSP Path Found:")
    print(csp_path)
    print("Steps:", len(csp_path) - 1)

else:
    print("No path found")
 # -----------------------
# Decision Making Agent
# -----------------------

print("\n----- Decision Making Agent -----")

agent = DecisionAgent()

best_algo, best_path, score = (
    agent.choose_best_path(
        bfs_path,
        dfs_path,
        ucs_path,
        astar_path,
        csp_path
    )
)

print("Best Algorithm:", best_algo)
print("Best Path:", best_path)
print("Utility Score:", score)
print("Steps:", len(best_path) - 1)

# -----------------------
# Uncertainty Handling
# -----------------------

print("\n----- Reasoning Under Uncertainty -----")

uncertainty = (
    UncertaintyHandler()
)

best_algo_uncertain, probability = (
    uncertainty.predict_success(
        bfs_path,
        dfs_path,
        ucs_path,
        astar_path,
        csp_path
    )
)

print("\nBest Predicted Algorithm:")
print(best_algo_uncertain)

print(
    "Success Probability:",
    probability * 100,
    "%"
)
# -----------------------
# Maze Visualization GUI
# -----------------------

print("\nOpening Maze GUI...")

# Show best path visually
gui = MazeGUI(
    maze,
    best_path
)