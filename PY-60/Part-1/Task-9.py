# Даны два неотрицательных числа a и b.
# Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a·b)^1/2

def geometric_mean(a, b):
    g_mean = round((a*b) ** (1/2), 2)
    return g_mean


first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))
print(f"Среднее геометрическое: {geometric_mean(first_num, second_num)}")
