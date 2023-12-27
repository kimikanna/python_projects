# Даны три целых числа: A, B, C. Проверить истинность высказывания:
# «Справедливо двойное неравенство A < B < C».

def is_true(number_a, number_b, number_c):
    return (number_a < number_b) and (number_b < number_c)


num_a = int(input('Enter a number A: '))
num_b = int(input('Enter a number B: '))
num_c = int(input('Enter a number C: '))
print(f'Statement "A < B < C" is {is_true(num_a, num_b, num_c)}')
