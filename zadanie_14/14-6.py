"""
В системе счисления с основанием N запись числа 8710 оканчивается на 2 и содержит не более двух цифр.
Перечислите через запятую в порядке возрастания все подходящие значения N.
"""
for n in range(3, 100):
    x = 87
    s = ''
    while x > 0:
        s = str(x % n) + s
        x //= n
    if s[-1] == '2' and len(s) <= 2:
        print(s, n)