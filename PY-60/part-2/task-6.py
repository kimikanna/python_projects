# Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы). Для нахождения десятков
# использовать операцию деления нацело, для нахождения
# единиц — операцию взятия остатка от деления.

def get_tens(two_digit_number):
    tens = two_digit_number // 10
    return tens


def get_units(two_digit_number):
    units = two_digit_number % 10
    return units


number = int(input("Введите двузначное число: "))

print(f"Десятки: {get_tens(number)}")
print(f"Единицы: {get_units(number)}")
