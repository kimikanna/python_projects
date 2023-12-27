# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Хотя бы одно из чисел A и B нечетное».

def is_at_least_one_of_them_odd(number_a, number_b):
    return (number_a % 2 == 1) or (number_b % 2 == 1)


num_a = int(input('Enter a number A: '))
num_b = int(input('Enter a number B: '))
print(f'Statement "at least one of A and B is odd" is {is_at_least_one_of_them_odd(num_a, num_b)}')
