# Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.

def get_reversed_digits(two_digit_number):
    reversed_digits = two_digit_number // 10 + (two_digit_number % 10 * 10)
    return reversed_digits


number = int(input("Введите двузначное число: "))
print(f"Результат перестановки цифр: {get_reversed_digits(number)}")
