# print("y x z w F")
# for y in range(0,2):
#     for x in range(0,2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 Function = ((not y and x) or (not z or not w)) and ((w or x) or y)
#                 # Function = ((not y and x) or (not z or not w)) and ((w or x) or y)
#                 if Function == 0:
#                     print(x, y, z, w, Function)


# V - оба пункта равны 0 или 1
#

# n = 1
# s = 0
# while n <= 300:
#     s = s + 30
#     n = n * 5
# 5, 25, 125, 625
# 30, 60, 90, 120
# print(s)

# s = 0
# n = 0

# while s < 165:
#     s += 15
#     n += 2
#
# # 0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150
# # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22
# print(n)

# n = 4
# s = 0
# while n <= 8:
#     s += n
#     n += 1
# s=4, 9, 15, 22, 30
# n=5, 6, 7, 8, 9
# print(s)

# n = 50
# s = 1
# while s < 1000:
#     print("start:", s, n)
#     s *= 2
#     n += 10
#     print('stop:', s, n)

# s = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
# n = 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150
# print(n)

# s = 0
# n = 0
#
# while 2 * s * s < 123:
#    s = s + 1
#    n = n + 3
#    print(2 * s * s, n)

# s=0, 2, 6, 18, 32, 50, 72, 98, 128
# n=3, 6, 9, 12, 15, 18, 21, 24
# print(n)

# s = 22
# n = 0
# while s < s * s:
#     s = s - 1
#     n = n + 3
# s = 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# n = 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63
# print(n)
# s = 0
# k = 1
#
# while s < 66:
#     k += 3
#     s += k
# # s=0, 4, 11, 21, 34, 50, 69
# # k=1, 4, 7, 10, 13, 16, 19, 22, 25
# print(k)
# x = int(input())
# for i in range(0, 1000):
#     x = i
#     L = 0
#     M = 0
#     while x > 0:
#         M = M + 1
#         if (x % 2) != 0:
#             L = L + x % 8
#         x = x // 8
#     if L == 14 and M == 3:
#         print(i)
#         # print(L)
#         # print(M)

# for i in range(0, 100000):
#     x = i
#     a, b = 0, 0
#     while x > 0:
#         a = a + 1
#         b = b + x % 100
#         x = x // 100
#     if a == 2 and b == 13:
#         print(i)

# file = open("17.txt", "r")
# strings = []
# for i in file.readlines():
#     strings.append(int(i))
#
# count = 0
# m = 0
# for i in range(len(strings) - 1):
#     for j in range(i + 1, len(strings)):
#         if strings[i] * strings[j] % 26 == 0:
#             count += 1
#         m = max(m, strings[i] + strings[j])
#
# print(count, m)
# count = m = 0
#
# f = open('17.txt')
# l = [int(i) for i in f]
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] % 26 == 0:
#             count += 1
#         m = max(m, l[i] + l[j])
#
# print(count, m)

# f = open("26.txt", "r")
# mass_and_count = f.readline()
# l = [int(i) for i in f.readlines()]
# l = sorted(l)
# print(l[1612:-1])
# mass, count = mass_and_count.split(" ")
# container_mass = 0
# container_count = 0
# much_mass = 0
# for i in range(int(count)):
#     print(i)
#     if container_mass >= int(mass):
#         much_mass = l[i]
#         break
#     container_mass += l[i]
#     container_count += 1
# print(container_count, much_mass)

# def F(n):
#     if n > 0:
#         G(n - 1)
#
#
# def G(n):
#     print("*")
#     if n > 1:
#         F(n - 3)

# F(11)
# G=10 6 2
# * * *
# F=7 3 -1

#def factorial(n):
#    if n == 1:
#        return n
#    print(f"{n} * {n - 1}")
#    return n * factorial(n - 1)

# 5
# 5 * func(4)
# 4
# 4 * func(3)
# 3
# 3 * func(2)
# 2
# 2 * func(1)
# 1
# 1
# 1 * 2 * 6 * 24 * 120
#print(factorial(5))

def F(n):
    if n < 8:
        F(n + 3)
        print(n)
        F(2 * n)


F(1)
