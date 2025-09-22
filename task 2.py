tiket_nomber = input()
if (int(tiket_nomber) >=100_000) and (int(tiket_nomber) < 1_000_000):
    if int(tiket_nomber[0])+int(tiket_nomber[1])+int(tiket_nomber[2]) == int(tiket_nomber[4])+int(tiket_nomber[5])+int(tiket_nomber[3]):
        print("Счастливый билет")
    else: print("Несчастливый билет")
else: print("ошибка введенных данных")