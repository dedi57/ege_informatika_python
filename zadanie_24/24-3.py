"""
Текстовый файл 24-5.txt содержит последовательность из символов «(»и «)», всего не более 10**6 символов.
Определите максимальное количество подряд идущих открывающих скобок «(» в этом файле.
"""
with open('../files/24/24-5.txt') as f:
    s = f.readline()
    kmax = 0
    k = 1
    for i in range(1, len(s)):
        if s[i] == '(' and s[i-1] == '(':
            k += 1
            if k > kmax:
                kmax = k
        else:
            k = 1
    print(kmax)