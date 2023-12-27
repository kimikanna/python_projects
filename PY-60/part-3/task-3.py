# Дано целое число A. Проверить истинность высказывания: «Число A является четным».

def is_even(number_a):
    return number_a % 2 == 0


num_a = int(input('Enter a number: '))
print(f'Statement "Number A is even" is {is_even(num_a)}')
