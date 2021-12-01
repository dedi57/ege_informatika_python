'''
(П. Волгин) Значение выражения (7**160 • 7**90) – (14**150 + 2**13) записали в системе счисления с основанием 7.
Найдите сумму всех цифр семеричной записи числа, исключая шестерки.
'''
f = (7 ** 160 * 7 ** 90) - (14 ** 150 + 2 ** 13)
summa = 0
while f > 0:
    if f % 7 != 6:
        summa += f % 7
    f //= 7
print(summa)