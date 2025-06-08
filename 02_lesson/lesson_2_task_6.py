def month_to_season(month):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if len(winter) == 3 and month in winter:
        return "Зима"
    elif len(spring) == 3 and month in spring:
        return "Весна"
    elif len(summer) == 3 and month in summer:
        return "Лето"
    elif len(autumn) == 3 and month in autumn:
        return "Осень"
    else:
        return "Некорректный номер месяца"

# Примеры вызова


print(month_to_season(2))   # Зима
print(month_to_season(4))   # Весна
print(month_to_season(8))   # Лето
print(month_to_season(11))  # Осень
print(month_to_season(13))  # Некорректный номер месяца
