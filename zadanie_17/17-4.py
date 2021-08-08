"""
Рассматривается множество целых чисел, принадлежащих отрезку [1107; 9504], которые делятся на 9 и
не делятся на 7, 15, 17 и 19. Найдите количество таких чисел и минимальное из них.
В ответе запишите два числа через пробел: сначала количество, затем минимальное число.
"""
s = []
for n in range(1107, 9505):
    if n % 9 == 0:
        if n % 7 != 0 and n % 15 != 0 and n % 17 != 0 and n % 19 != 0:
            s.append(n)
print(len(s), min(s))