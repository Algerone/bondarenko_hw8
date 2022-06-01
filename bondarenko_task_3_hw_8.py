"""Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.
Пример(Example)
Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]"""

user_input: list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]

print(sorted(user_input, key=lambda i: i[1]))
