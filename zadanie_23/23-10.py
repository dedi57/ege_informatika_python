'''
У исполнителя Калькулятор две команды, которым присвоены номера:
1. прибавь 1
2. увеличь число десятков на 1
Например, при помощи команды 2 число 23 преобразуется в 33. Если перед выполнением команды 2 вторая с конца цифра
равна 9, она не изменяется. Сколько есть программ, которые число 10 преобразуют в число 33?
'''
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x + 10, y)
print(f(10, 33))