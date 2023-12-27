# Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».

def is_odd(number_a):
    return number_a % 2 == 1


num_a = int(input('Enter a number: '))
print(f'Statement "Number A is odd" is {is_odd(num_a)}')
