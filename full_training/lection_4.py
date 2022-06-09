# string = 123
#
#
# # Есть ли хоть 1 число
# def isString(string_on_check):
#     if isinstance(string_on_check, str):
#         print("ЭТО 100% СТРОКА.")
#     return False
#
# # if type(string_on_check) == str:
# #     return True
# # else:
# #     return False
#
#
# def isNumber(string_in_function):
#     if isString(string_in_function):
#         print("Это строка.")
#     else:
#         print("Это фигня какая-то")
#
#     for i in string_in_function:
#         try:
#             int(i)
#         except ValueError:
#             continue
#         return True
#     return False
#
#
# print(isNumber(string))

# def toType(string, type_to=str):
#     print(type_to(string))
#
#
# toType(0)
# toType(123)
# toType(123)
# toType(123)
# toType(123)

# def get_on_list(index=0, list_of_data=None):
#     if list_of_data is None:
#         list_of_data = []
#     print(list_of_data)
#     # return list_of_data[index]
#
#
# get_on_list(list_of_data=[1, 2, 3], index=4)
# get_on_list(list_of_data=[1])

string1 = "24242dasdasfdas"
string2 = "asdasdasdsadas34"
string3 = "adsdasdasd"


def isNumber(string_to_work=None):
    for i in string_to_work:
        try:
            int(i)
        except ValueError:
            continue
        print("Число е")
    print("Числа немае")


# isNumber(string1)
# isNumber(string2)
# isNumber(string3)
# print(isNumber.__code__)
