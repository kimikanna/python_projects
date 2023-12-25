# Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру
# данного числа (сотни).

def get_hundreds(three_digit_number):
    hundreds = three_digit_number // 100
    return hundreds

number = int(input("Введите трёхзначное число: "))
print(f"Первая цифра числа: {get_hundreds(number)}")
