# Дано двузначное число. Найти сумму и произведение его цифр.

def get_sum_of_digits(two_digit_number):
    sum_of_digits = (two_digit_number // 10) + (two_digit_number % 10)
    return sum_of_digits


def get_product_of_digits(two_digit_number):
    product_of_digits = (two_digit_number // 10) * (two_digit_number % 10)
    return product_of_digits


number = int(input("Введите двузначное число: ta"))
print(f"Сумма чисел: {get_sum_of_digits(number)}")
print(f"Произведение чисел: {get_product_of_digits(number)}")
