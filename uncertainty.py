# uncertainty.py

import random


class UncertaintyHandler:

    def __init__(self):
        pass

    # Generate probability score
    def calculate_probability(self, path):

        if not path:
            return 0

        # Simple probability logic
        probability = round(
            random.uniform(0.70, 0.99),
            2
        )

        return probability

    # Predict path success
    def predict_success(
            self,
            bfs_path,
            dfs_path,
            ucs_path,
            astar_path,
            csp_path
    ):

        algorithms = {

            "BFS": bfs_path,
            "DFS": dfs_path,
            "UCS": ucs_path,
            "A*": astar_path,
            "CSP": csp_path
        }

        best_algorithm = None
        highest_probability = 0

        for algo, path in algorithms.items():

            if path:

                probability = (
                    self.calculate_probability(
                        path
                    )
                )

                print(
                    f"{algo} Success Probability:"
                    f" {probability * 100}%"
                )

                if probability > highest_probability:

                    highest_probability = (
                        probability
                    )

                    best_algorithm = algo

        return (
            best_algorithm,
            highest_probability
        )