# Калькулятор

import tkinter as tk

def get_values():
    num1 = int(number1_entty.get())
    num2 = int(number2_entty.get())
    return num1, num2

def insert_values(value):
    answer_entty.delete(0, 'end')
    answer_entty.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sud():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sud)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250, y=200)
number1_entty = tk.Entry(window, width=28)
number1_entty.place(x=100, y=75)
number2_entty = tk.Entry(window, width=28)
number2_entty.place(x=100, y=150)
answer_entty = tk.Entry(window, width=28)
answer_entty.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое чичсло:')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе чичсло:')
number2.place(x=100, y=125)
answer = tk.Label(window, text='Результат:')
answer.place(x=100, y=275)
window.mainloop()