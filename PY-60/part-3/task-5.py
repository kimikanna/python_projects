# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A >= 0 или B < −2».

def is_true(number_a, number_b):
    return (number_a > 0) or (number_b <= -2)


num_a = int(input('Enter a number A: '))
num_b = int(input('Enter a number B: '))
print(f'Statement "A >= 0 or B < -2" is {is_true(num_a, num_b)}')
