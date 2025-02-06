experience = int(input("Введите число ?"))

# Какое значение переменной level должно быть задано изначально? 
level = 1 

# Проверки каких условий должна выполнить программа? Напишите их ниже.
if experience >= 5000:
    level = 4
elif experience >= 2500:
    level = 3
elif experience >= 1000:
    level = 2
print('Уровень персонажа:', level)
