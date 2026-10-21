
import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])

            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)

    return distance


def solve():
    queue = [(heuristic(start), 0, start, [])]
    visited = set()

    while queue:
        f, cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            print("Solution found!")

            for s in path:
                for i in range(0, 9, 3):
                    print(s[i:i+3])
                print()

            print("Total moves:", len(path) - 1)
            return

        zero = state.index(0)
        r, c = zero // 3, zero % 3

        for dr, dc in [(1, 0), (-1, 0),
                       (0, 1), (0, -1)]:

            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)

                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )

                new_state = tuple(new_state)

                if new_state not in visited:
                    new_cost = cost + 1

                    heapq.heappush(
                        queue,
                        (
                            new_cost + heuristic(new_state),
                            new_cost,
                            new_state,
                            path
                        )
                    )


solve()
