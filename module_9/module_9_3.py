# "Генераторные сборки"


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
a = list(zip(first, second))
first_result = (abs(len(x[0])-len(x[1])) for x in zip(second, first) if len(x[0]) != len(x[1]))
second_result = (bool(len(first[x]) == len(second[x])) for x in range(len(first)))
try:
    print(list(first_result))
    print(list(second_result))
except IndexError as exc:
    print(f'Списки должны быть одной длины, {exc}')
except TypeError as exc:
    print(f'Списки должны состоять из строк, {exc}')