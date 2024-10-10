# Рекурсивное умножение цифр

# мое решение без переводов в строки
def get_multiplied_digits_v2(number):
    if number // 10 == 0: # еслил осталась крайняя чифра числа
        return number % 10 # возвращаем крайнюю цифру числа
    elif number % 10 == 0: # пропускаем нули
        return get_multiplied_digits_v2(number // 10) #
    else: # производим перемножение цифр числа
        return number % 10 * get_multiplied_digits_v2(number // 10)

# решение по заданию
def get_multiplied_digits(number):
    if number == 0: # проверка на вшивость )))
        return 0
    str_number = str(number).replace('0', '')  # переводим число в строку + убираем все 0
    # т.к. я так и не нашел пока решения с числами оканчивающимися на 0 (10, 20, 100 и т.д)
    first = int(str_number[0])  # присваиваем first первый элемент
    if len(str_number) > 1: # если длина строки больше 1
        return first * get_multiplied_digits(int(str_number[1:])) # возвращаем
    else:
        return int(str_number[0]) # иначе возвращаем оставшийся элемент строки

test = [0, 1, 10, 402, 42001, 40203]
for i in test:
    print('Проверка числа', i)
    print(f'Результат работы функции согласно заданию: {get_multiplied_digits(i)}')
    print(f'Результат работы функции мое решение: {get_multiplied_digits_v2(i)}')