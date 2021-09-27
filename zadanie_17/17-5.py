'''
В файле 17-1.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые
значения от -10 000 до 10 000 включительно. Определите и запишите в ответе сначала количество пар элементов
последовательности, в которых хотя бы одно число делится на 7, а другое при этом не делится на 17.
Затем - минимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих
подряд элемента последовательности.
Например, для последовательности -45; 14; 22; -21; 34 ответом будет пара чисел: 3 и -31.
'''
with open('../files/17/17-1.txt') as f:
    s, s1 = [], []
    for x in f:
        s.append(int(x))
    for i in range(1, len(s)):
        if (s[i] % 7 == 0 and s[i-1] % 17 != 0) or (s[i-1] % 7 == 0 and s[i] % 17 != 0):
            s1.append(s[i] + s[i-1])
    print(len(s1), min(s1))