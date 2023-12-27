# 2. Дана сторона квадрата a. Найти его площадь {{S = a^2}}

def area_of_the_square(a):
    area = round(a**2, 2)
    return area


side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата со стороной {side}: {area_of_the_square(side)}")
