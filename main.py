print('3x^2+5x+7 Числа 3,5,7 - коэффициенты уравнения')
equation = input('Введите коэффициенты a b c через пробел: ').split()

n1 = int(equation[0])
n2 = int(equation[1])
n3 = int(equation[2])

def Discriminant(a,b,c):
    d = (b**2) + (-4*a*c)
    if d < 0:
        return -1
    else:
        return d


d = Discriminant(n1,n2,n3)


if d < 0:   # Проверка на наличие корней
    print('Корней нет')
else:
    for x in range(1, d**2):    # Нахождение корня из Дискриминанта
        if x*x == d:
            d = x
            break


    x1 = (-n2 + d) / (2*n1) # Находим 1 корень
    x2 = (-n2 - d) / (2*n1) # Находим 2 корень
    if x1 == x2: # Сравниваем если корни равны выводим только 1 из них
        print('x = ' + str(x1))
    else:
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))

