users = ["Дмитрий", 'Диана', 'Данил']
users.append("13")  # В КОНЕЦ
users.insert(0, "13")  # ПО ПЕРВОМУ ЗНАЧЕНИЮ
users.extend([1, 2, 3])
print("12" in users)
print(len(users))
print(users.count("13"))
print(users.index("Данил"))
print(users)

a = {1, 2, 3, 4}
b = {1, 5, 4, 4}
print(a.intersection(b))
print({1, 2, 3})

a = {"key": "value", "value": "key111", "fas": "ro", "duh": "druh"}
print(list(a.items()))  # keys, values, items

if "Данил" in users:
    print("УРА ДАНИЛУ")
elif "Диана" in users:  # else if
    print("ура диане")
elif "Диана" in users:  # else if
    print("ура диане")
elif "Диана" in users:  # else if
    print("ура диане")
else:
    print("--")

j = b = 1
print(id(j))
print(id(b))
print(j is b)
a = "STOP" if b == 0 else "GO"
print(a)
