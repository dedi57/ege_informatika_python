"""
Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 3
3. Возвести в квадрат
Программа для исполнителя Калькулятор – это последовательность команд.
Сколько существует программ, для которых при исходном числе 2 результатом является число 19?
"""
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if y**0.5 == round(y** 0.5):
        return f(x, y-1) + f(x, y - 3) + f(x, y**0.5)
    return f(x, y-1) + f(x, y - 3)

print(f(2, 19))