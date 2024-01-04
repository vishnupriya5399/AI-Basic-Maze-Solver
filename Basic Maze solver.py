from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = (0, 0)
        self.end = (self.rows - 1, self.cols - 1)
        self.graph = self._build_graph()
        self.visited = set()

    def _is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == 0

    def _get_neighbors(self, node):
        row, col = node
        return [(row + dr, col + dc) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)] if self._is_valid_move(row + dr, col + dc)]

    def _build_graph(self):
        graph = {}
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == 0:
                    node = (row, col)
                    neighbors = [neighbor for neighbor in self._get_neighbors(node)]
                    graph[node] = neighbors
        return graph

    def solve_maze_dfs(self):
        path = self._dfs(self.start, [])
        self._print_solution(path)

    def _dfs(self, node, path):
        if node == self.end:
            return path + [node]

        self.visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                new_path = self._dfs(neighbor, path + [node])
                if new_path:
                    return new_path

        return []

    def solve_maze_bfs(self):
        path = self._bfs()
        self._print_solution(path)

    def _bfs(self):
        queue = deque([(self.start, [])])
        self.visited.add(self.start)

        while queue:
            current, path = queue.popleft()

            if current == self.end:
                return path + [current]

            for neighbor in self.graph[current]:
                if neighbor not in self.visited:
                    queue.append((neighbor, path + [current]))
                    self.visited.add(neighbor)

        return []

    def _print_solution(self, path):
        if not path:
            print("No solution found.")
            return

        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) == self.start:
                    print("S", end=' ')
                elif (row, col) == self.end:
                    print("E", end=' ')
                elif (row, col) in path:
                    print(".", end=' ')
                elif self.maze[row][col] == 1:
                    print("#", end=' ')
                else:
                    print(" ", end=' ')
            print()


# Example Maze (0 represents open path, 1 represents wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Create MazeSolver object and solve the maze using DFS and BFS
solver = MazeSolver(maze)

print("DFS Solution:")
solver.solve_maze_dfs()

print("\nBFS Solution:")
solver.solve_maze_bfs()
