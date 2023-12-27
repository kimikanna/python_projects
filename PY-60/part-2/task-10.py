# Дано трехзначное число. Вывести вначале его последнюю цифру (единицы),
# а затем — его среднюю цифру (десятки).

def get_hundreds(three_digit_number):
    hundreds = three_digit_number // 100
    return hundreds


def get_tens(three_digit_number):
    tens = three_digit_number % 100 // 10
    return tens


number = int(input("Введите трёхзначное число: "))
print(f"Первая цифра числа: {get_hundreds(number)}")
print(f"Вторая цифра числа: {get_tens(number)}")
