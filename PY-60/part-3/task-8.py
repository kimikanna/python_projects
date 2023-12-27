# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Каждое из чисел A и B нечетное».

def is_both_odd(number_a, number_b):
    return (number_a % 2 == 1) and (number_b % 2 == 1)


num_a = int(input('Enter a number A: '))
num_b = int(input('Enter a number B: '))
print(f'Statement "both A and B are odd" is {is_both_odd(num_a, num_b)}')
