# "Декораторы"


def is_prime(function):
    def simple(*args):
        result = function(*args)
        for i in range(2, result // 2 + 1):
            if not result % i:
                return f'Составное \n{result}'
        else:
            return f'Простое \n{result}'
    return simple


@is_prime
def sum_three(*args):
    result = sum(args)
    return result


# Пример:

result = sum_three(2, 3, 6, 6)
print(result)