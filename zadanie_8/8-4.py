"""Тимофей составляет 5-буквенные коды из букв Т, И, М, О, Ф, Е, Й. Буква Й может использоваться в коде
не более одного раза, при этом она не может стоять на первом месте, на последнем месте и рядом с буквой И.
Все остальные буквы могут встречаться произольное количество раз или не встречаться совсем.
Сколько различных кодов может составить Тимофей?
"""
letters = 'ТИМОФЕЙ'
k = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if word.count('Й') < 2 and 'ИЙ' not in word and 'ЙИ' not in word and word[0] != 'Й' and word[-1] != 'Й':
                        k += 1
print(k)