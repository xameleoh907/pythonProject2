# Распаковка

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# print_params() # вызов функции с параметрами по умолчанию
# print_params(b = 25) # параметру b присваивается 25, параиетры а и с по умолчанию
# print_params(c = [1,2,3]) #параметру c присваивается строка [1,2,3], параметры а и b по умолчанию
# print_params(False) #параметру а присваивается False, параметры с и b по умолчанию
# print_params(*['Anton', 'Dima', 'Max']) # распаковка списка с 3 элементами
# # print_params(b = ['a=3', 'b=4', 'c=5'], *['Z', 8]) # ошикба, список ['Z', 8] распаковывается в параметры а и b
# # нельзя передать параметру b дополнительно список ['a=3', 'b=4', 'c=5']
# print_params(**{'a': 3, 'b': 'Anton', 'c': True}) # распаковка словаря
# # print_params(1, 2, 3, 4) # ошибка, нельзя передать больше параметров, чем определено функцией
# # print_params(a=5, d=6, c=7) # ошибка, параметр d не определен функцией

values_list = [True, 'Anton', 1234]
values_dict = {'a': 'Max', 'b': (1,2), 'c': False}
# print_params(*values_list) # распаковка списка
# print_params(**values_dict) # распаковка словаря

values_list_2 = ['Moscow', 123]
values_list_3 = [True]
values_dict_2 = {'b': 'Evgen', 'c': 52}
# print_params(*values_list_2, 42) #работает, values_list_2 распокавался и передал 2 параметра а и b, параметру с присвоино 42
# print_params(*values_list_3, **values_dict_2) # распаковка списка и словаря
# # print_params(**values_dict_2, *values_list_3) # ошибка **kwargs перед *args
# # print_params(**values_dict_2, 42) # ошибка позиции аргумента
# print_params(42, **values_dict_2) # распаковка аргумента и словаря