
from collections import deque

def water_jug():
    capacity1 = 4
    capacity2 = 3

    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == 2 or b == 2:
            print("Solution:")
            for state in path:
                print(state)
            return

        amount = min(a, capacity2 - b)
        amount2 = min(b, capacity1 - a)

        states = [
            (capacity1, b),             # Fill jug 1
            (a, capacity2),             # Fill jug 2
            (0, b),                     # Empty jug 1
            (a, 0),                     # Empty jug 2
            (a - amount, b + amount),   # Pour jug 1 into jug 2
            (a + amount2, b - amount2)  # Pour jug 2 into jug 1
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("Solution not found")


water_jug()
