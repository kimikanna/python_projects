# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 2 и B <= 3».

def is_true(number_a, number_b):
    return (number_a > 2) and (number_b <= 3)


num_a = int(input('Enter a number A: '))
num_b = int(input('Enter a number B: '))
print(f'Statement "A > 2 and B <= 3" is {is_true(num_a, num_b)}')
