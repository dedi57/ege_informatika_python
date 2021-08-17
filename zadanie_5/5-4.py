"""Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N-1.
2) Инвертируются все разряды исходного числа (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Для какого значения N результат работы алгоритма равен 18?
"""
for i in range(0, 256):
    x = str(bin(i-1))[2:]
    if len(x) < 8:
        x = (8-len(x)) * '0' + x
    x1 = ''
    for s in x:
        if s == '0':
            x1 += '1'
        else:
            x1 += '0'
    if int(x1, 2) == 18:
        print(i)