# Дана сторона квадрата a. Найти его периметр P = 4·a
def perimeter_of_the_square(a):
    perimeter = round(a * 4, 2)
    return perimeter


side = float(input("Введите сторону квадрата: "))
print(f"Периметр квадрата со стороной {side}: {perimeter_of_the_square(side)}")
