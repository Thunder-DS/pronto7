import math

# Ввод
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисление дискриминанта
D = b**2 - 4*a*c

# Проверка условий и нахождение корней
if D>0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Корни:", x1, "и", x2)
elif D==0:
    x = -b/(2*a)
    print("Корень:", x)
else:
    print("Нет корней")
