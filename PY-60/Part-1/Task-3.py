# 3. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)

def area_of_the_rectangle(a, b):
    area = round(a * b, 2)
    return area


def perimeter_of_the_rectangle(a, b):
    perimeter = round(2 * (a+b), 2)
    return perimeter


side_a = float(input("Введите длину квадрата: "))
side_b = float(input("Введите ширину квадрата: "))
print(f"Площадь прямоугольника со сторонами {side_a} и {side_b}: {area_of_the_rectangle(side_a, side_b)}")
print(f"Периметр прямоугольника со сторонами {side_a} и {side_b}: {perimeter_of_the_rectangle(side_a, side_b)}")
