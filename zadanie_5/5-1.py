'''
Алгоритм получает  на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
1. Вычисляется сумма чётных цифр в десятичной записи числа N. Если четных цифр в записи нет, сумма считается равной нулю.
2. Вычисляется сумма цифр, стоящих на чётных местах в десятичной записи числа N без ведущих нулей. Места отсчитываются
слева направо (от старших разряов к младшим, начиная с единицы). Если число однозначное (цифр на чётных местах нет),
сумма считается равной нулю.
3. Результатом работы алгоритма становится модуль разности полученных двух сумм.
При каком наименьшем N в результате работы алгоритма получится R = 13?
'''
for n in range(10, 1000):
    number = str(n)
    s1, s2 = 0, 0
    for x in number:
        if int(x) % 2 == 0:
            s1 += int(x)
    for i in range(1, len(number), 2):
        s2 += int(number[i])
    if abs(s2 - s1) == 13:
        print(n)