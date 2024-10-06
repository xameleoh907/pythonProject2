# Я твой матрица вертел
def rotation_matrix (matrix_in, rot): # не будем лишать себя радости вращать матрицу больше, чем 90 градусов
# функция принимает матрицу matrix_in и количество оборотов rot
    matrix_out = [] # создаем пустой список
    if rot % 4 == 0: # по правде матрица будет вращаться не более 3х раз
        matrix_out = matrix_in # разворот на 360 градусов
    else:
        for i in range(rot % 4): # развороот на (rot % 4)*90 градусов
            matrix_out = [] # обнуляем матрицу
            m = len(matrix_in) # строки
            n = len(matrix_in[0]) # столбцы
            for i in range(len(matrix_in[0])): # первый цикл считаем по количеству столбцов
                row = [None] * len(matrix_in) # заполняем список пустыми значениями по количеству строк
                k = len(matrix_in) - 1 # обратный счетчик индексов
                for j in range(len(matrix_in)): # второй цикл по считаем по количеству строк
                    row[j] = matrix_in[k][i] # заполняем список со смещением, согласно повороту матрицы
                    k -= 1 # уменьшаем счетчик
                matrix_out.append(row) # добавляем смещенный список в новую матрицу
            matrix_in = matrix_out # передаем новое положение матрицы matrix_in для дальнейшего вращения
    return matrix_out # возвращаем матрицу
def print_matrix (p_matrix): # функция для наглядного и красивого отображения матрицы
    for i in p_matrix:
        print (*i)
def rand_matrix (m, n): # создание m x n размерной матрици
    r_matrix = []
    for i in range(m):
        r_row = []
        for j in range(n): # заполняем матрицу значениями индексов в формаие 11
            r_row.append((i+1)*10+j+1)
        r_matrix.append(r_row)
    # можно было подключить рондом, но так наглядней
    return r_matrix # возвращаем раполненную матрицу размером m x n
print('Добро пожаловать в программу по вращению матриц')
line = int(input('Введите количестко строк матрицы: '))
column = int(input('Введите количество столбцов матрицы: '))
rotat = int(input('Введите на какое число оборотов по часовой стрелке повернуть матрицу (1 оборот = 90 градусов): '))
matrix = rand_matrix(line, column)
print('Матрица до переворота')
print_matrix(matrix)
print(f'Матрица после переворота на { rotat*90} градусов')
result = rotation_matrix(matrix, rotat)
print_matrix(result)
print('Спасибо, что выбрали нашу вращалку')