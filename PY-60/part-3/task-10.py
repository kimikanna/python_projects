# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Ровно одно из чисел A и B нечетное»

def is_exactly_one_of_them_odd(number_a, number_b):
    return (number_a % 2 == 1) ^ (number_b % 2 == 1)


num_a = int(input('Enter a number A: '))
num_b = int(input('Enter a number B: '))
print(f'Statement "exactly one of A and B is odd" is {is_exactly_one_of_them_odd(num_a, num_b)}')
