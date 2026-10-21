import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

h = {'A': 5, 'B': 4, 'C': 4,
     'D': 3, 'E': 1, 'F': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                new_cost = cost + weight
                heapq.heappush(
                    pq,
                    (new_cost + h[neighbour],
                     new_cost,
                     neighbour,
                     path + [neighbour])
                )

astar('A', 'F')
