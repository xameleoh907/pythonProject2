# Счётчик вызовов
def count_calls (): # счетчик вызова фукций
    global \
        calls
    calls += 1 # увеличиваем глабальную переменную каждый раз при вызове функции


def string_info(string_f): # функция сбора сведений строки
    count_calls() # вызов счетчика функций
    str_info = (len(string_f), string_f.upper(), string_f.lower()) # создание кортежа с данными
    return str_info # возвращаем кортеж


def is_contains(string, list_): # функция поиска строки в списке
    count_calls() # вызов счетчика функций
    for i in list_: # перебор строки
        if string.upper() in i.upper(): # поик совпадений
            is_contains_f = True
        else:
            is_contains_f = False
    return is_contains_f # возвращаем результат поиска


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)