"""
Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (111)
    заменить(111, 2)
    заменить(222, 3)
    заменить(333, 1)
  КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 130 единиц?
"""
s = 130 * '1'
while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('222', '3', 1)
    s = s.replace('333', '1', 1)
print(s)