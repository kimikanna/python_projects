# Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально
# возможное количество отрезков длины B (без наложений). Используя операцию деления нацело,
# найти количество отрезков B, размещенных на отрезке A.

def get_quantity_of_b_in_a(a, b):
    quantity = a // b
    return quantity


a = int(input("Введите количество отрезков A: "))
b = int(input("Введите количество отрезков B: "))

print(f"Количество отрезков B, размещенных на отрезке A: {get_quantity_of_b_in_a(a, b)}")