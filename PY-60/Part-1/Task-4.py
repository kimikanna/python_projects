# Дан диаметр окружности d. Найти ее длину {{L = π·d, π = 3.14}}

PI = 3.14


def calculate_circle_length(d):
    length = round(PI * d, 2)
    return length


diameter = float(input("Введите диаметр: "))
print(f"Длина окружности: {calculate_circle_length(diameter)}")
