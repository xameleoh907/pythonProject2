# "Вызов разом"


def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        result[function.__name__] =  function(int_list)
    return result


# Пример работы кода:
try:
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    print(apply_all_func(['б', 20, 15, 9], max, min))
except (TypeError, NameError) as exc:
    print(f'Введены недопустимые данные: {exc}')