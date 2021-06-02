"""
Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя
три команды, которым присвоены номера:
1. прибавь 1
2. прибавь 2
3. прибавь следующее
Первая из них увеличивает число на экране на 1, вторая увеличивает это число на 2,
а третья прибавляет к числу на экране число, большее на 1.
Программа для исполнителя Калькулятор– это последовательность команд.
Сколько есть программ, которые число 2 преобразуют в число 10?
"""

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if y % 2 != 0:
        return f(x, y-1) + f(x, y-2) + f(x, (y-1) // 2)
    return f(x, y-1) + f(x, y-2)

print(f(2, 10))