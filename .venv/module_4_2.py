# "Пространство имен"

def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()
#inner_function() # ошибка, т.к. inner_function() находится в области видимости test_function() и не существует за её пределами
