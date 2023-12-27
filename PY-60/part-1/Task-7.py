# Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R^2, π=3.14

PI = 3.14


def calculate_circle_length(r):
    length = round(2 * PI * r, 2)
    return length


def calculate_circle_area(r):
    area = round(PI * r**2, 2)
    return area


radius = float(input("Введите радиус: "))
print(f"Длина окружности: {calculate_circle_length(radius)}")
print(f"Площадь круга: {calculate_circle_area(radius)}")
