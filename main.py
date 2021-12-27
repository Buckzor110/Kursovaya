from tkinter import *
from tkinter import scrolledtext
import math

window = Tk()
window.geometry('600x400')
window.title("Добро пожаловать в курсовую работу Егора Ершова")


def choose():
    global txt
    spce = Label(window, text=" ", font=('Comic Sans', 10))
    spce.grid(column=0, row=9)
    inputlbl = Label(window, text="Введите элементы:", font=('Comic Sans', 10))
    inputlbl.grid(column=0, row=10)
    txt = Entry(window, width=40)
    txt.grid(column=1, row=10)
    inpbtn = Button(window, text="Ввод", command=algoritm)
    inpbtn.grid(column=2, row=10)


def algoritm():
    global txt
    items = list(txt.get())
    spce = Label(window, text=" ", font=('Comic Sans', 10))
    spce.grid(column=0, row=11)
    lbl = Label(window, text="Все возможные сочетания:", font=('Comic Sans', 10))
    lbl.grid(column=0, row=12)
    intalg(items)


def intalg(x):
    global txt1
    out = scrolledtext.ScrolledText(window, width=40, height=10)
    out.grid(column=1, row=13)
    source = x
    elm = len(source)
    cells = int(txt1.get())
    if elm < cells:
        out.insert(INSERT, 'Позиций не может быть больше элементов')
        return
    res = []
    arrang = math.factorial(elm) / (math.factorial(elm-cells) * math.factorial(cells))
    for i in range(int(arrang)):
        res.append([])
        tempsource = source[:]
        for j in range(cells):
            p = i // math.factorial(cells - 1 - j) % len(tempsource)
            res[len(res) - 1].append(tempsource[p])
            tempsource.pop(p)
    for i in range(len(res)):
        out.insert(INSERT, res[i])
        out.insert(INSERT, '\n')


mainlbl = Label(window, text="Алгоритм генерации всех сочетаний", font=50)
mainlbl.grid(column=1, row=0)

txt1 = Entry(window, width=20)
txt1.grid(column=1, row=7)

lbl = Label(window, text="Выберите количество позиций: ", font=('Comic Sans', 10))
lbl.grid(column=0, row=7)

spce = Label(window, text=" ", font=('Comic Sans', 10))
spce.grid(column=0, row=6)

btn = Button(window, text="Выбрать", command=choose)
btn.grid(column=2, row=7)

window.mainloop()