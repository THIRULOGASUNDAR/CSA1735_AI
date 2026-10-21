
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [
    (1, 0), (2, 0), (0, 1),
    (0, 2), (1, 1)
]


def valid(m, c):
    mr = 3 - m
    cr = 3 - c

    return (
        0 <= m <= 3 and 0 <= c <= 3
        and (m == 0 or m >= c)
        and (mr == 0 or mr >= cr)
    )


def solve():
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if dm + dc >= 1 and valid(
                new_state[0], new_state[1]
            ):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(
                        (new_state, path + [new_state])
                    )

    print("Solution not found")


solve()
