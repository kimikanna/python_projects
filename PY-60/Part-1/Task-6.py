# Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)

def volume(a, b, c):
    v = round(a*b*c, 2)
    return v


def surface_area(a, b, c):
    s = round(2 * (a*b + b*c + a*c), 2)
    return s


side_a = float(input("Введите длину параллелепипеда: "))
side_b = float(input("Введите ширину параллелепипеда: "))
side_c = float(input("Введите высоту параллелепипеда: "))

print(f"Объём параллелепипеда: {volume(side_a, side_b, side_c)}")
print(f"Площадь поверхности параллелепипеда: {surface_area(side_a, side_b, side_c)}")
