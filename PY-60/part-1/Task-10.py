# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

def operations_with_two_numbers(a, b):
    result = [None] * 4
    result[0] = round(a**2 + b**2, 2)
    result[1] = round(a**2 - b**2, 2)
    result[2] = round(a**2 * b**2, 2)
    result[3] = round(a**2 / b**2, 2)
    return result


first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))
operations = operations_with_two_numbers(first_num, second_num)
print(f"Сумма квадратов: {operations[0]}")
print(f"Разность квадратов: {operations[1]}")
print(f"Произведение квадратов: {operations[2]}")
print(f"Частное квадратов: {operations[3]}")
