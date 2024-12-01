# "Функциональное разнообразие"
from random import choice

# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'
result_lambda = list(map(lambda x, y: x == y, first, second))

print('Пример работы Lambda-функции:')
print(result_lambda)


# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                if not isinstance(data, str):
                    data = str(data)
                file.write(data + '\n')
    return write_everything

#Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

print('\nПример работы метода __call__:')
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


