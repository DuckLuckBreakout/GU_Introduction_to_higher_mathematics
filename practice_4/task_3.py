"""
На листе тетради «в линейку» (расстояние между линиями равно а) лежит игла (длиной b). 
Координаты нижней точки иглы (х,у), игла лежит под углом alfa. Пересекает ли игла линию или нет?
"""

from math import pi, sin

a = 3
b = 1
alpha = pi/2

(x, y) = (3, 2.1)

height = b * sin(alpha)

if y//a < (y + height)//a:
    print('Пересекает')
else:
    print('Не пересекает')


