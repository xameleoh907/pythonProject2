# Задача "Матрица воплоти"
def get_matrix (n, m, value): # функция создания матрицы get_matrix
    matrix = [] # создаем пустой список matrix
    for i in range(n): # первый цикл по количеству строк
        row = [] # создаем пустой список со столбцами
        for j in range(m): # второй цикл по количеству столбцов
            row.append(value) # добавляем в список row значение value по количеству столбцов
        matrix.append(row) # добавляем в матрицу matrix строку
    return matrix # возвращаем матрицу
# ввод данных от пользователя
line = int(input('Введите количество строк матрицы: '))
column = int(input('Введите количество столбцов матрицы: '))
element = int(input('Введите элемент матрицы: '))
result = get_matrix(line, column, element)
print('Результат работы функции: ')
print(result)