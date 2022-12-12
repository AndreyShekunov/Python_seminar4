# Задача 1. Вычислить число Пи c заданной точностью d
# Например:
#     при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

from math import pi

d = input('Введите d = ')
print(f'Число Пи = {pi}')
len_d = len(d.split('.')[1]) # определяем длину после 1 цифры и точки
print(f'Число пи с точностью {d} = ', end='')
i = 0
num_pi = str(pi) # превращаем Пи в строку
while i < (len_d + 2) and i < len(num_pi): 
    print(num_pi[i], end='')
    i += 1