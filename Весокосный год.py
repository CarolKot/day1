#year = int(input('Введите год ?'))
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
 #   print('Год вес')
#elif year % 400 == 0:
 #   print('Год вес')
#else:
 #   print('Год невес')


#year = int(input('Введите год ?'))
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#    print('Год вес')
#else:
#    print('Год невес')

#n = int(input('Введите год? '))
#if n % 100 == 0:
#    if n % 400 == 0:
#       print ("YES")
#    else:
#        print("NO")
#else:
#    if n % 4 == 0:
#        print ("YES")
#    else:
#        print('NO')
#print ("")

n = int(input("Введите года ? "))
if n % 400 == 0:
    print("YES")
elif n % 100 == 0:
    print("NO")
elif n % 4 ==0:
    print("YSE")
else:
    print("NO")
