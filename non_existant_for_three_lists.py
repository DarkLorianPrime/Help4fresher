a, b, c = [1, 3, 4, 5], [3, 4, 6, 7], [6, 7, 5, 8]
found_numbers = []

for i in range(0, len(a)):
    if a[i] not in set(b) | set(c) and a.count(a[i]) == 1:
        found_numbers.append(a[i])

    if b[i] not in set(c) | set(a) and b.count(b[i]) == 1:
        found_numbers.append(b[i])

    if c[i] not in set(a) | set(b) and c.count(c[i]) == 1:
        found_numbers.append(c[i])

print(found_numbers)
