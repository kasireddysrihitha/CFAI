# decision_agent.py


class DecisionAgent:

    def __init__(self):
        pass

    # Calculate utility score
    def calculate_utility(
            self,
            path_length,
            risk=0,
            priority=1
    ):

        # Utility Formula
        utility = (
            path_length
            + risk
            - priority
        )

        return utility

    # Select Best Path
    def choose_best_path(
            self,
            bfs_path,
            dfs_path,
            ucs_path,
            astar_path,
            csp_path
    ):

        paths = {}

        # Add paths if available
        if bfs_path:
            paths["BFS"] = bfs_path

        if dfs_path:
            paths["DFS"] = dfs_path

        if ucs_path:
            paths["UCS"] = ucs_path

        if astar_path:
            paths["A*"] = astar_path

        if csp_path:
            paths["CSP"] = csp_path

        best_algorithm = None
        best_score = float("inf")
        best_path = None

        # Compare all paths
        for algo, path in paths.items():

            path_length = len(path)

            score = self.calculate_utility(
                path_length
            )

            if score < best_score:
                best_score = score
                best_algorithm = algo
                best_path = path

        return (
            best_algorithm,
            best_path,
            best_score
        )