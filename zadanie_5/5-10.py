'''
(Джобс) Автомат обрабатывает натуральное число N по следующему алгоритму.
1. Строится двоичная запись числа N.
2. Если N четное, то в конец полученной записи (справа) дописывается 0, в начало— 1; если N— нечётное в конец и начало дописывается по две единицы.
3. Результат переводится в десятичную систему и выводится на экран.

Укажите наименьшее число, большее 52, которое может является результатом работы автомата.
'''
numbers = []
for n in range(1, 1000):
    if n % 2 == 0:
        s = '1' + bin(n)[2:] + '0'
    else:
        s = '11' + bin(n)[2:] + '11'
    if int(s, 2) > 52:
        numbers.append(int(s, 2))
print(min(numbers))