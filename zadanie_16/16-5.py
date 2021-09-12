'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n, при n ≤ 3
при n > 3:
  F(n) = n + 3 + F(n–1), при чётном n;
  F(n) = n*n + F(n-2), при нечётном n;
Определите количество натуральных значений n на отрезке [1; 1000], при которых F(n) кратно 7.
'''

k = 0
def f(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return n + 3 + f(n - 1)
        else:
            return n * n + f(n - 2)

for i in range(1, 1001):
    if f(i) % 7 == 0:
        k += 1
print(k)
