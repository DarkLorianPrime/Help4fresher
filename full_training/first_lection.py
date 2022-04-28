str()  # "23"
int()  # 123
float()  # 0.1
bool()  # True\False
list()  # [123,123,123]
tuple()  # (123,123,123)
dict()  # {"123": "1"}
set()  # {1,2,4,5,6,7}

# func()
# class()

a = 123254324
print(a)
float = 1.1
print(a + float)
complex = 1 + 2j
print(complex)
bools = 1 == 1
print(bools)

str = "sad \"PRIVET\" "
print(str)
list_s = ["1", "5", "10", "9"]
1, 5, 10, 9
print(list_s)
list_s.append("6")
print(list_s)
tuple_s = (5, 6, 7)


def func(a, b, c):
    print(a)
    print(b)
    print(c)


func((1, 2, 4), 1, 2)
dict
HB = {
    (1, 2): "09.01.2001",
    "Евгений": "01.09.2009"
}
print(HB.get((1, 2), "Значение в словаре не найдено."))

B = [1, 1, 1, 1, 1, 9, 1, 2, 3, 4, 5, 1, 1, 1, 5, 2]
B = list(set(B))
print(B)
a = 10
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
a = a ** b  # 10^6
b = a ** b  # 10^6^6
print(b)
['h', 'e', 'l', 'l', 'o']
name = "Дима"
surname = "Дмитриев"
last_name = "Дима"
print("Мое имя - {} {} {}".format(name, surname, last_name))
print("Мое имя - {named} {surnamed} {last_named}".format(named=name, surnamed=surname, last_named=last_name))
print(f"Мое имя - {name} {surname} {last_name}")
print("Мое имя - " + name + " " + surname + " " + last_name)
print('fas''das')
listed = ['h', 'e', 'l', 'l', 'o', "!"]
# True | False
print(False == 0)
print(True == 1)
a = 1
if a == 5:
    print("1")
elif a == 6:
    print("2")
else:
    print(3)


def func():
    print(1)


def func2():
    print(2)


less = {
    "1": "1"
}


def error():
    print("Элемент не найден.")


less["1"]()  # Crash
print(less)
less["0"] = func
print(less)
less["0"]()  # Call
less.get("0", error)()  # If not found
name = input(">>> ")
sp = ["A", "B", "C"]
print('привет', 'мир', sep=" ")


def text_complete(text):
    return text + "."


print(text_complete("DATA"))

i = 0
j = 5
a = [1, 5, 10, 5, 10, 5]
print(a[0:5])
####################################

# Передать в функцию 5 значений, и внутри функции убрать повторяющиеся. Вернуть список.
# Функция передлывающая переданные значения (НЕ ОТДЕЛЬНЫЙ СПИСОК) в множитель (Кортеж -> Мн)
def tuple_to_set(list_of_data):
    new_list_of_data = list_of_data.copy()
    new_list_of_data.append("CHTO-TO")
    return new_list_of_data, list_of_data


print(tuple_to_set([0, 1, 2, 3, 4, 5]))
###### EGE #####
s = int(input())
n = 1
while s < 47: # 26
    s = s + 4
    n = n * 2
    print(s, n)
print(n)
