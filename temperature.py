temperature = int(input("Какая температу на датчике? "))
double = 0
problem = 0 
while True:
    if double != temperature:
        print(f'{temperature}')
        double = temperature
        temperature = int(input("Какая температу на датчике? "))
        if temperature == double:
            problem +=1
            print(f'Внимание: дублирующее значение температуры {double} обнаружено!')
            print(f'Зафиксировано сбоев датчика:{problem}')
            question = int(input("Хотите продолжить сбор данных? "))
            if question == 0:
               print(f'Сбор данных остановлен')
               break
            elif question == 1:
                temperature = int(input("Какая температу на датчике? "))