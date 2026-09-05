import time
import heapq
from collections import deque

# =========================================================
# DELIVERY ROUTE GRAPH
# =========================================================

graph = {
    "Warehouse": {
        "Distribution Center": 80,
        "Sorting Center": 100,
        "Local Hub": 150
    },
    "Distribution Center": {
        "Customer": 200
    },
    "Sorting Center": {
        "Customer": 180
    },
    "Local Hub": {
        "Customer": 100
    },
    "Customer": {}
}

# =========================================================
# HEURISTIC VALUES
# =========================================================

h = {
    "Warehouse": 250,
    "Distribution Center": 200,
    "Sorting Center": 180,
    "Local Hub": 100,
    "Customer": 0
}

START = "Warehouse"
GOAL = "Customer"

# =========================================================
# 1. BREADTH FIRST SEARCH - UNINFORMED SEARCH
# =========================================================

def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    nodes = 0

    while queue:
        current, path, cost = queue.popleft()
        nodes += 1

        if current == goal:
            return path, cost, nodes

        if current in visited:
            continue

        visited.add(current)

        for location, distance in graph[current].items():
            if location not in visited:
                queue.append(
                    (location, path + [location], cost + distance)
                )

    return None, 0, nodes

# =========================================================
# 2. DEPTH FIRST SEARCH - UNINFORMED SEARCH
# =========================================================

def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    nodes = 0

    while stack:
        current, path, cost = stack.pop()
        nodes += 1

        if current == goal:
            return path, cost, nodes

        if current in visited:
            continue

        visited.add(current)

        neighbours = list(graph[current].items())
        neighbours.reverse()

        for location, distance in neighbours:
            if location not in visited:
                stack.append(
                    (location, path + [location], cost + distance)
                )

    return None, 0, nodes

# =========================================================
# 3. GREEDY BEST-FIRST SEARCH - INFORMED SEARCH
# =========================================================

def greedy(start, goal):
    current = start
    path = [current]
    cost = 0
    visited = set()
    nodes = 0

    while current != goal:
        visited.add(current)
        nodes += 1

        candidates = [
            location for location in graph[current]
            if location not in visited
        ]

        if not candidates:
            return None, 0, nodes

        next_location = min(
            candidates,
            key=lambda location: h[location]
        )

        cost += graph[current][next_location]
        current = next_location
        path.append(current)

    nodes += 1
    return path, cost, nodes

# =========================================================
# 4. A* SEARCH - INFORMED SEARCH
# =========================================================

def a_star(start, goal):
    priority_queue = [
        (h[start], 0, start, [start])
    ]

    best_cost = {start: 0}
    nodes = 0

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)
        nodes += 1

        if current == goal:
            return path, g, nodes

        for location, distance in graph[current].items():
            new_cost = g + distance

            if location not in best_cost or new_cost < best_cost[location]:
                best_cost[location] = new_cost
                new_f = new_cost + h[location]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_cost, location, path + [location])
                )

    return None, 0, nodes

# =========================================================
# 5. HILL CLIMBING - LOCAL SEARCH
# =========================================================

def hill_climbing(start, goal):
    current = start
    path = [current]
    cost = 0
    nodes = 0

    while current != goal:
        nodes += 1

        neighbours = list(graph[current].items())

        if not neighbours:
            return None, 0, nodes

        next_location, distance = min(
            neighbours,
            key=lambda item: h[item[0]]
        )

        if h[next_location] >= h[current]:
            return None, cost, nodes

        cost += distance
        current = next_location
        path.append(current)

    nodes += 1
    return path, cost, nodes

# =========================================================
# 6. N-QUEENS - CONSTRAINT SATISFACTION
# =========================================================

def solve_n_queens(n):
    board = [-1] * n
    nodes = 0

    def is_safe(row, col):
        for previous_row in range(row):
            previous_col = board[previous_row]

            if previous_col == col:
                return False

            if abs(previous_col - col) == abs(previous_row - row):
                return False

        return True

    def backtrack(row):
        nonlocal nodes
        nodes += 1

        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row] = col

                if backtrack(row + 1):
                    return True

                board[row] = -1

        return False

    start_time = time.perf_counter()
    solved = backtrack(0)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return solved, board, nodes, execution_time

# =========================================================
# PERFORMANCE TESTING
# =========================================================

def test_algorithm(name, function):
    start_time = time.perf_counter()

    path, cost, nodes = function(START, GOAL)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("\n" + "-" * 55)
    print("Algorithm:", name)
    print("-" * 55)

    if path:
        print("Path:", " -> ".join(path))
        print("Total Cost:", cost, "km")
    else:
        print("No solution found")

    print("Nodes Explored:", nodes)
    print("Execution Time:", round(execution_time, 8), "seconds")

# =========================================================
# MAIN PROGRAM
# =========================================================

print("=" * 60)
print("SEARCH ALGORITHM PERFORMANCE EVALUATION")
print("=" * 60)

test_algorithm(
    "Breadth First Search - Uninformed Search",
    bfs
)

test_algorithm(
    "Depth First Search - Uninformed Search",
    dfs
)

test_algorithm(
    "Greedy Best-First Search - Informed Search",
    greedy
)

test_algorithm(
    "A* Search - Informed Search",
    a_star
)

test_algorithm(
    "Hill Climbing - Local Search",
    hill_climbing
)

# =========================================================
# N-QUEENS TEST
# =========================================================

print("\n" + "=" * 60)
print("CONSTRAINT SATISFACTION - N QUEENS")
print("=" * 60)

n = 4

solved, board, nodes, execution_time = solve_n_queens(n)

if solved:
    print("N =", n)
    print("Solution:", board)
    print("Nodes Explored:", nodes)
    print("Execution Time:", round(execution_time, 8), "seconds")
else:
    print("No solution found")
