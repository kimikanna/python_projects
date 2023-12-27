# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2

def average(a, b):
    avg = round((a + b) / 2, 2)
    return avg


first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))
print(f"Среднее арифметическое: {average(first_num, second_num)}")
