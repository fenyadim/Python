#! python3

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import ttk
from PIL import Image, ImageTk

isTO = ['Заготовка', 'Отжиг', 'ТО']
isNoTO = ['Заготовка']


def clicked():
    result.delete(1.0, END)
    report = []
    if varTerm.get() == 0:
        for i in range(len(isTO)):
            report.append(isTO[i])
    else:
        report.append(isNoTO[0])
    report.append(varDetail.get())
    for i in range(len(report)):
        if report[i] == 'ТО':
            item = report[i]
            report.append(item)
            report.remove(report[i])
        report[i] = str(i + 1) + '. ' + str(report[i]) + '\n'
        result.insert(str(len(report)) + '.0', report[i])


def toggleOption():
    global squareOptionFrame
    global roundOptionFrame
    if varDetail.get() == 0:
        squareOptionFrame.pack_forget()
        roundOptionFrame.pack()
    else:
        roundOptionFrame.pack_forget()
        squareOptionFrame.pack()


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400')
img = Image.open('TP/type_1.png')
img = img.resize((212, 78), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Vars
varTerm = IntVar()
varDetail = IntVar()
varOptionRound = IntVar()

# Frames
firstFrame = LabelFrame(window, text='Первый шаг. Закалка')
secondFrame = LabelFrame(window, text='Второй шаг. Деталь')

# Tabs
tab_control = ttk.Notebook(secondFrame)
roundTab = ttk.Frame(tab_control)
squareTab = ttk.Frame(tab_control)
tab_control.add(roundTab, text='Пруток')
tab_control.add(squareTab, text='Блок')
tab_control.pack()

roundOptionFrame = Frame(roundTab)
squareOptionFrame = Frame(roundTab)

# tab_control_roundTab = ttk.Notebook(roundTab)
# type1 = ttk.Frame(tab_control_roundTab)
# type2 = ttk.Frame(tab_control_roundTab)
# tab_control_roundTab.add(type1, image=img)
# tab_control_roundTab.add(type2, image=img)
# tab_control_roundTab.pack()

# Radio buttons
rad1 = Radiobutton(firstFrame, text='Есть', value=0,
                   variable=varTerm, command=clicked)
rad2 = Radiobutton(firstFrame, text='Нет', value=1,
                   variable=varTerm, command=clicked)
rad3 = Radiobutton(roundTab, image=img,  value=0,
                   variable=varDetail, command=toggleOption)
rad4 = Radiobutton(roundTab, text='Невращающаяся',
                   value=1, variable=varDetail, command=toggleOption)
r_Square = Radiobutton(squareOptionFrame, text='r_Square')
r_Round = Radiobutton(roundOptionFrame, text='r_Round')
r_Round.pack()

# Result Text
result = Text()

# Positions
firstFrame.pack()
secondFrame.pack()
# roundOptionFrame.pack()
# squareOptionFrame.pack()
rad1.pack(side=LEFT)
rad2.pack(side=RIGHT)
rad3.pack(side=LEFT)
rad4.pack(side=RIGHT)
r_Square.pack()
result.pack()

window.mainloop()
