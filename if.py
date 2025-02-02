pogoda = int(input("Какая погода на улице ?"))
if pogoda >= 30:
    print("Relly hott")
elif pogoda >= 20:
    print("Warm")
elif pogoda >= 10:
    print("Chilly")
else:
    print("Cold")