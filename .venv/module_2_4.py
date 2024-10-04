# Задача "Всё не так уж просто"
numbers = []
primes = []
not_primes = []
if int(input('Для введения своего списка нажмите 1, для решения задания нажмите 0: ')) == 0:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
else:
    while True:
        numbers_in = int(input('Введите значение, для завершения введите 0: '))
        if numbers_in != 0:
            numbers.append(numbers_in)
        else:
            break
print('Список значений для проверки: ', numbers)
numbers = set(sorted(numbers))
numbers = list(numbers)
if numbers[0] == 1:
    primes.append(numbers[0])
    numbers.pop(0)
for i in range(len(numbers)):
    is_prime = True
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Список простых чисел: ', primes)
print('Список составных чисел: ', not_primes)
