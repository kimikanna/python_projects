# Дано целое число A. Проверить истинность высказывания: «Число A является положительным».

def is_positive(number_a):
    return number_a > 0


num_a = int(input('Enter a number: '))
print(f'Statement "Number A is positive" is {is_positive(num_a)}')
