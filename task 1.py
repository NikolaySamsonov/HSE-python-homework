year = int(input())
if (year >= 1000) and (year <= 10000):
    if year % 4 == 0:
        print("Високосный год")
    else: print("Обычный год")
else: print("Ошибка введенных данных")