import math
while True:
    try:
        x = float(input("Введіть число х: "))
        n = int(input("Введіть число n: "))
        break
    except:
        print("Wrong input")
d = 1.0
f = 1
i = 0  # ітератор
n = n*2  # збільшення діапазону вдвічі
for i in range(2, n+2, 2):
    d *= x  # обрахунок х в степені n
    f *= i*(i-1)  # обрахунок факторіала
    a = d / f
    print(a, end=' ')  # виведення 
    i = i+2

