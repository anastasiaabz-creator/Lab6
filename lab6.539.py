a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

common_keys = set(a.keys()) & set(b.keys())
print(*common_keys)

