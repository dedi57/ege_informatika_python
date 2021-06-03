"""
Текстовый файл 24-3.txt содержит последовательность из строчных и заглавных букв английского алфавита и цифр,
всего не более 10**6 символов. Возрастающей подпоследовательностью будем называть последовательность символов,
расположенных в порядке увеличения их номера в кодовой таблице символов ASCII.
Определите длину наибольшей возрастающей подпоследовательности.
"""
with open('../files/24/24-3.txt') as f:
    s = f.readline()
    k = 1
    kmax = 0
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            k += 1
            if k > kmax:
                kmax = k
        else:
            k = 1
    print(kmax)