ABC = [500, 100, 2000, 30000, 400000, 535, 52436, 647, 898, 90785, 1340]
ABC_s = {500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
ABC_t = (500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

i = 0

while i < len(ABC):
    # print(ABC[i])
    i += 1

for x in ABC_s: # ПОКА НЕ ПРИГОДИТСЯ.
    for y in ABC_t:
        for z in ABC:
            pass
            # print(x, y, z)

dict_of_data = {1: 2, 3: 4}
i = 0
z = 0
# for k, i in enumerate(ABC):
#     print(k, i)
#     if i == 500:
#         z = k
# print(z)
# for k, v in dict_of_data.items():
#     print(i)
string = "Дед пошел за яблоками, но не вернулся. Его съели волки."
string_new = ""
string_d = string.split()
string_d[0] = "Дядя"
print(" - загадал я, ".join(["1", "2", "3"]) + " - загадал я")
# for i in string:
#     if i.lower() == "д":
#         string_new += "$"
#     else:
#         string_new += i
# print(string_new)
# name = "ivan"
# surname = "ivanovich"
# name.
# print(name.capitalize() + surname.capitalize())

# lower, upper, islower, isupper, capitalize
# continue, break
d = []
for i in range(1, 10):
    if i % 2 == 0:
        print("I - четное")
        break
    d.append(i)
print(d)

spisok = list(range(0, 10))

for k, i in enumerate(spisok):
    if i % 2 == 0:
        spisok[k] = i * 10

print(spisok)
while True:
    pass
