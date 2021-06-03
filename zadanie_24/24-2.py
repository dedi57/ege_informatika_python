"""
Текстовый файл 24-s1.txt состоит не более чем из 10**6 заглавных латинских букв (A..Z).
Текст разбит на строки различной длины.
Определите количество строк, в которых встречается комбинация A*R, где звёздочка обозначает любой символ.
"""
with open('../files/24/24-s1.txt') as f:
    k = 0
    while True:
        s = f.readline()
        if not s:
            break
        for i in range(0, len(s) - 2):
            if s[i] == 'A' and s[i+2] == 'R':
                k += 1
                break
print(k)
