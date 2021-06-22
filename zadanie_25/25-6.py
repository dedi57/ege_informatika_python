"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [258274; 258297], числа,
имеющие ровно 4 различных делителя.
Выведите для каждого найденного числа два наибольших делителя в порядке возрастания.
"""
for i in range(258274, 258298):
    divs = set()
    for d in range(1, round(i**0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(divs)