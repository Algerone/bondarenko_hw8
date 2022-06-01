"""Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них"""

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


def max_value(arg1: int, arg2: int, arg3: int) -> int:
    """function compare 3 arguments and return max value"""
    return max(arg1, arg2, arg3)


print(max_value(int_numbers[0], int_numbers[1], int_numbers[2]))
