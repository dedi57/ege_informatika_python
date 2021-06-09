"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [154026; 154043], числа,
имеющие ровно 4 различных делителя.
В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.
"""
for i in range(154026, 154044):
    divs = []
    for d in range(1, i+1):
        if i % d == 0:
            divs.append(d)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(divs[2], divs[3])