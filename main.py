import math
while True:
    try:
        x = float(input("Введіть число х: "))
        n = int(input("Введіть число n: "))
        break
    except:
        print("Wrong input")
d = 1.0  # обрахунок х в степені n
f = 1  # обрахунок факторіала
i = 0  # ітератор
n = n*2  # збільшення діапазону вдвічі
lst = []  # масив для запису результату
for i in range(2, n+2, 2):
    d *= x
    f *= i*(i-1)
    a = d / f
    lst.append(a)
    i = i+2
print(lst)






