# Дана масса M в килограммах. Используя операцию деления нацело,
# найти количество полных тонн в ней (1 тонна = 1000 кг).

def get_tons(kilograms):
    tons = kilograms // 1000
    return tons


kgs = int(input("Введите количество килограммов: "))
print(f"Количество тонн: {get_tons(kgs)}")
