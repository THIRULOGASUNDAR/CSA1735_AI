tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"]
}

values = {
    "D": 3, "E": 5,
    "F": 2, "G": 9
}

def minimax(node, maximizing):
    if node not in tree:
        return values[node]

    results = [
        minimax(child, not maximizing)
        for child in tree[node]
    ]

    if maximizing:
        return max(results)
    else:
        return min(results)

result = minimax("A", True)
print("Best value for MAX:", result)
