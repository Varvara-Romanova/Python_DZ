import math


def square(side):
    # Проверяем, является ли сторона целым числом
    if isinstance(side, int):
        return side * side
    else:
        # Округляем вверх и вычисляем площадь
        rounded_side = math.ceil(side)
        return rounded_side * rounded_side

# Примеры вызова функции


print(square(5))      # 25
print(square(4.3))    # 25 (4.3 → 5 → 5*5)
print(square(7.9))    # 64 (7.9 → 8 → 8*8)
