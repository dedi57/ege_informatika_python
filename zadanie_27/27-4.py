"""
Набор данных состоит из нечетного количества пар натуральынх чисел. Необходимо выбрать из каждой пары ровно одно
число так, что бы чётность суммы выбранных чисемл совпадала с чётностью большинства выбранных чисел и при этом сумма
выбранных чисел была как можно меньше. Определите минимальную сумму которую можно получить при таком выборе.
"""
with open('../files/27/s27-B.txt') as f:
    n = f.readline()
    summa, chet, nechet = 0, 0, 0
    for x in f:
        a, b = map(int, x.split())
        m = min(a, b)
        summa += m
        if m % 2 == 0:
            chet += 1
        else:
            nechet += 1
        if a % 2 != b % 2:

    print(summa)
    print(summa % 2)
    print(chet, nechet)