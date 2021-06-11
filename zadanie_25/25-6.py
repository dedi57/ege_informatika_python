"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [164700; 164752], числа,
имеющие ровно 6 различных делителей.
В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.
"""
for i in range(164700, 164753):
    divs = []
    for d in range(1, i+1):
        if i % d == 0:
            divs.append(d)
            if len(divs) > 6:
                break
    if len(divs) == 6:
        print(divs[4], divs[5])

