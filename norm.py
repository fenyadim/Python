#! python3

from tkinter import *
from tkinter import ttk

data = [[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        [25, 2.7, 3, 3.3, 3.6, 3.9, 4.2, 0, 0, 0, 0],
        [50, 3.1, 3.5, 3.9, 4.3, 4.7, 5.1, 0, 0, 0, 0],
        [100, 3.8, 4.3, 4.8, 5.3, 5.8, 6.3, 6.8, 0, 0, 0]]
i_X = 0
i_Y = 0


def showResult():
    global i_X, i_Y
    for i in range(len(data[0])):
        if int(ent_diameter.get()) <= int(data[0][i]):
            i_Y = i
            break
    for j in range(len(data)):
        if int(ent_lenght.get()) <= int(data[j][0]):
            i_X = j
            break
    if i_X == 0 or i_Y == 0 or data[i_X][i_Y] == 0:
        result.configure(text='Не может быть')
    else:
        result.configure(text=data[i_X][i_Y])


# General
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')

# Tabs
tab_control = ttk.Notebook(window)
turningOperation = ttk.Frame(tab_control)
tab_control.add(turningOperation, text='Токарная')
tab_control.pack(expand=1, fill='both')

# Text
lbl_diameter = Label(
    turningOperation, text='Диаметр').grid(column=0, row=0)
ent_diameter = Entry(turningOperation, width=10)
ent_diameter.grid(column=1, row=0)
lbl_lenght = Label(
    turningOperation, text='Длина валика').grid(column=0, row=1)
ent_lenght = Entry(turningOperation, width=10)
ent_lenght.grid(column=1, row=1)
result = Label(turningOperation)
result.grid(column=0, row=2)
btn = Button(turningOperation, text='Рассчитать',
             command=showResult).grid(column=0, row=3)

window.mainloop()
