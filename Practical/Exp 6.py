rooms = {'A': 'Dirty', 'B': 'Dirty'}
position = 'A'

while 'Dirty' in rooms.values():
    print("Vacuum at", position)

    if rooms[position] == 'Dirty':
        rooms[position] = 'Clean'
        print(position, "cleaned")

    else:
        position = 'B' if position == 'A' else 'A'

print("All rooms cleaned")
print(rooms)
