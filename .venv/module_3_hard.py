# "Раз, два, три, четыре, пять .... Это не всё?"

import tkinter as tk

def converter (*list_f): # конвертов все простые элементы переводит в int, массивы в list
    if isinstance(list_f[0], bool):
        data = int(list_f[0])
    elif isinstance(list_f[0], list) or isinstance(list_f[0], int) or isinstance(list_f[0], float):
        data = list_f[0]
    elif isinstance(list_f[0], tuple) or isinstance(list_f[0], set):
        data = list(list_f[0])
    elif isinstance(list_f[0], dict):
        data = list(list_f[0].items())
    elif isinstance(list_f[0], str):
        data = len(list_f[0])
    return data

def calculate_structure_sum(*list_f): # подсчет суммы xbctk и длин строк
    summator = 0
    element_ = converter(list_f[0])
    if  isinstance(element_, int):
        return element_
    else:
        for i in element_:
            element_f = converter(i)
            if  isinstance(element_f, int):
                summator += element_f
            else:
                summator += calculate_structure_sum(i)
        return summator

def res (): # обработка кнопки "расчитать"
    data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
    result = calculate_structure_sum(data_structure)
    res_str = 'Сумма чисел и длин строк равна:  ' + str(result)
    lbl_res.configure(text=res_str)


window = tk.Tk()
window.title('module_3_hard.py')
window.geometry('350x350')
window.resizable(False, False)
lbl = tk.Label(window, text='Раз, два, три, четыре, пять .... Это не всё?', font=("Arial Bold", 12))
lbl.place(x=10, y=0)
tasks_lbl = tk.Label(window, text="data_structure = [\n[1, 2, 3],\n{'a': 4, 'b': 5},\n(6, {'cube': 7, 'drum': 8}),\n'Hello',\n((), [{(2, 'Urban', ('Urban2', 35))}])\n]", font=("Arial Bold", 14))
tasks_lbl.place(x=40, y=50)
button_res = tk.Button(window, text='Расчитать', width=20, height=2, font=("Arial Bold", 12), command=res)
button_res.place(x=80, y=220)
lbl_res = tk.Label(window, text='Сумма чисел и длин строк равна:', font=("Arial Bold", 12))
lbl_res.place(x=10, y=300)
window.mainloop()

# для вывода в консоль раскоментировать все ниже
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
