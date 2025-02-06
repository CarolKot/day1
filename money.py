money = int(input("Введите вашу ЗП : "))

while money > 0:
    num = int(input("Сколько потратили?"))
    money -= num
    print(f'Увас осталось {money} денег!')
print(f'Денег нет!')

