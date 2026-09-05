# AI-Search-Algorithms-Delivery-Route-Optimization

### Practical Title

**Evaluate the performance of various algorithms (Uninformed, Informed, Local Search and Constraint Satisfaction) of problem solving through Search.**

---

## 1. Aim

To implement and evaluate different Artificial Intelligence search algorithms and compare their performance based on:

* Path found
* Total path cost
* Number of nodes explored
* Execution time

The practical implements:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Greedy Best-First Search
4. A* Search
5. Hill Climbing
6. N-Queens using Backtracking

---

## 2. Problem Statement

Implement various search algorithms used in Artificial Intelligence for solving problems through search.

The algorithms are categorized as:

| Category                | Algorithm                   |
| ----------------------- | --------------------------- |
| Uninformed Search       | Breadth First Search        |
| Uninformed Search       | Depth First Search          |
| Informed Search         | Greedy Best-First Search    |
| Informed Search         | A* Search                   |
| Local Search            | Hill Climbing               |
| Constraint Satisfaction | N-Queens using Backtracking |

The algorithms are evaluated using a **delivery route optimization problem**, where the objective is to find a path from the **Warehouse to the Customer**.

---

## 3. Objectives

* To understand different search strategies used in Artificial Intelligence.
* To implement Uninformed Search algorithms.
* To implement Informed Search algorithms using heuristic functions.
* To implement Local Search using Hill Climbing.
* To solve a Constraint Satisfaction Problem using Backtracking.
* To compare search algorithms based on nodes explored, path cost, and execution time.

---

## 4. Algorithms Implemented

### 4.1 Breadth First Search (BFS)

BFS explores the search space level by level.

It uses a **Queue (FIFO)** data structure.

**Characteristics:**

* Uninformed search
* Complete for finite search spaces
* Finds a solution with minimum number of edges
* Does not guarantee minimum path cost when edge costs are different

---

### 4.2 Depth First Search (DFS)

DFS explores one branch as deeply as possible before backtracking.

It uses a **Stack (LIFO)** data structure.

**Characteristics:**

* Uninformed search
* Memory efficient compared to BFS in many cases
* Does not guarantee an optimal path
* May explore a deep branch before finding a better solution

---

### 4.3 Greedy Best-First Search

Greedy Best-First Search uses a heuristic function to select the node that appears closest to the goal.

The evaluation function is:

```text
f(n) = h(n)
```

where:

* `h(n)` = estimated cost from the current node to the goal

**Characteristics:**

* Informed search
* Uses heuristic information
* Can reach the goal quickly
* Does not guarantee the optimal path

---

### 4.4 A* Search

A* Search uses both the actual path cost and the estimated cost to the goal.

The evaluation function is:

```text
f(n) = g(n) + h(n)
```

where:

* `g(n)` = actual cost from the start node
* `h(n)` = estimated cost to the goal
* `f(n)` = total estimated cost

**Characteristics:**

* Informed search
* Uses both path cost and heuristic
* Can find an optimal solution with a suitable heuristic
* More effective than uninformed search for suitable problems

---

### 4.5 Hill Climbing

Hill Climbing is a Local Search algorithm that selects the neighbouring state with the best heuristic value.

In this practical, the neighbour with the **lowest heuristic value** is selected.

**Characteristics:**

* Local search algorithm
* Uses heuristic information
* Requires less memory
* Can be fast for simple problems
* May get stuck at a local optimum

---

### 4.6 N-Queens using Backtracking

The N-Queens problem is solved as a **Constraint Satisfaction Problem (CSP)** using backtracking.

The objective is to place `N` queens on an `N × N` chessboard such that no two queens attack each other.

**Constraints:**

* No two queens should be in the same column.
* No two queens should be on the same diagonal.
* One queen is placed in each row.

For this practical:

```text
N = 4
```

---

## 5. Heuristic Values

The heuristic values used in the program are:

| Location            | Heuristic h(n) |
| ------------------- | -------------: |
| Warehouse           |            250 |
| Distribution Center |            200 |
| Sorting Center      |            180 |
| Local Hub           |            100 |
| Customer            |              0 |

---

## 6. Performance Evaluation

The algorithms are evaluated using the following parameters:

| Parameter       | Description                            |
| --------------- | -------------------------------------- |
| Path Found      | Route obtained by the algorithm        |
| Total Path Cost | Total distance travelled               |
| Nodes Explored  | Number of nodes processed              |
| Execution Time  | Time required to execute the algorithm |

Execution time is measured using:

```python
time.perf_counter()
```

---

## 7. Performance Comparison

| Algorithm         | Search Type  |  Path Cost | Nodes Explored | Execution Time |
| ----------------- | ------------ | ---------: | -------------: | -------------: |
| BFS               | Uninformed   | 250–280 km |       Measured |       Measured |
| DFS               | Uninformed   | 250–280 km |       Measured |       Measured |
| Greedy Best-First | Informed     |     250 km |       Measured |       Measured |
| A*                | Informed     |     250 km |       Measured |       Measured |
| Hill Climbing     | Local Search |     250 km |       Measured |       Measured |

**Note:** Nodes explored and execution time are measured automatically when the notebook is executed.

---

## 8. Analysis

Different AI search algorithms were applied to the delivery route problem.

* **BFS** searches level by level without heuristic information.
* **DFS** searches deeply but does not guarantee the optimal route.
* **Greedy Best-First Search** uses heuristic values to reach the goal quickly.
* **A*** uses both actual cost and heuristic cost to find an optimal route.
* **Hill Climbing** is fast but may get stuck at a local optimum.
* **N-Queens** uses backtracking to satisfy all constraints.

The optimal route for the given problem is:

```text
Warehouse → Local Hub → Customer
```

**Total Cost = 250 km**

---

## 9. Technologies Used

```text
Python
Jupyter Notebook
Artificial Intelligence
Search Algorithms
```

### Python Libraries

```python
import time
import heapq
from collections import deque
```

---

## 10. How to Run

```text
1. Clone or download the repository.
2. Open Delivery_Package_Route_Optimization.ipynb.
3. Open it using Jupyter Notebook or Google Colab.
4. Run all cells sequentially.
5. Observe the output.
6. Compare the performance of the algorithms.
```

---

## 11. Conclusion

The practical successfully implements different Artificial Intelligence search techniques.

**A*** is the most suitable algorithm for the delivery route problem because it considers both the actual path cost and the estimated cost to the goal.

The optimal route is:

```text
Warehouse → Local Hub → Customer
```

with a total cost of:

```text
250 km
```

The N-Queens problem is successfully solved using **Backtracking**, demonstrating the use of Constraint Satisfaction in Artificial Intelligence.

---



