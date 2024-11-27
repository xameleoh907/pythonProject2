# "План перехват"


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
    except ZeroDivisionError as exc:
        print(f'Ошибка деления {exc}')
        result = 0
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')
        result = None
    return result


#Пример выполнения программы:
# print(personal_sum("1, 2, 3"))
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
