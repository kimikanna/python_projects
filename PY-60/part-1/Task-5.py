# Дана длина ребра куба a. Найти объем куба V = a^3 и площадь его поверхности S = 6·a^2

def calculate_qube_volume(a):
    v = round(a**3, 2)
    return v


def calculate_qube_surface_area(a):
    s = round(6 * a**2, 2)
    return s


side = float(input("Введите сторону куба: "))
print(f"Объём куба: {calculate_qube_volume(side)}")
print(f"Площадь поверхности куба: {calculate_qube_surface_area(side)}")
