'''
Исполнитель Калькулятор преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 3
Программа для исполнителя Калькулятор – это последовательность команд. Сколько есть программ, которые число 7 преобразуют в число 20?
'''

def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y)


print(f(7, 20))