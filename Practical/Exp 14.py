tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"]
}
values = {
    "D": 3, "E": 5,
    "F": 2, "G": 9
}
pruned = []
def alphabeta(node, alpha, beta, maximizing):
    if node not in tree:
        return values[node]
    if maximizing:
        best = float("-inf")
        for i, child in enumerate(tree[node]):
            best = max(
                best,
                alphabeta(child, alpha, beta, False)
            )
            alpha = max(alpha, best)
            if alpha >= beta:
                pruned.extend(tree[node][i+1:])
                break
        return best
    else:
        best = float("inf")
        for i, child in enumerate(tree[node]):
            best = min(
                best,
                alphabeta(child, alpha, beta, True)
            )
            beta = min(beta, best)
            if beta <= alpha:
                pruned.extend(tree[node][i+1:])
                break
        return best
result = alphabeta(
    "A", float("-inf"), float("inf"), True
)

print("Best value for MAX:", result)
print("Pruned nodes:", pruned)
