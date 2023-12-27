# Дано расстояние L в сантиметрах. Используя операцию деления нацело,
# найти количество полных метров в нем (1 метр = 100 см).

def get_meters(centimeters):
    meters = centimeters // 100
    return meters


cm = int(input("Введите количество сантиметров: "))
print(f"Количество метров: {get_meters(cm)}")
