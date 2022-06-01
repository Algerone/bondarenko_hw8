"""Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать
3 аргумента и находить максимум с помощью функции1.
в итоге будет .
псевдокод
функция_нахождения_макс_из_2х(арг1, арг2):
return максимальное значение из 2х аргументов
функция_нахождения_макс_из_3х(арг1, арг2, арг3):
использую тут функция_нахождения_макс_из_2х()
return максимальное значение из 3х аргументов."""

user_numbers: list = input('Enter 3 digital numbers\n').split()  # пользователь вводит числа

while True:
    if len(user_numbers) != 3:  # проверя
        user_numbers: list = input('please enter 3 digital numbers\n').split()
        continue
    # print(not all([i.isdigit() for i in user_numbers]))
    # print([i.isdigit() for i in user_numbers])
    if not all(i.isdigit() for i in user_numbers):
        user_numbers: list = input('please enter 3 digital numbers\n').split()
        continue

    break

int_numbers: list = [int(i) for i in user_numbers]


def max_from_2(arg1: int, agr2: int) -> int:
    """function compare 2 arguments and return max value"""
    return max(arg1, agr2)


def max_value(arg1: int, arg2: int, arg3: int) -> int:
    """function compare 3 arguments and return max value using fuction max_from_2"""
    return max(
        max_from_2(arg1, arg2), max_from_2(arg2, arg3)
    )


print(max_value(int_numbers[0], int_numbers[1], int_numbers[2]))
