from tkinter import *
import math
import sys
root = Tk()
root['bg'] = '#d8e0dc'
root.title("Калькулятор")
root.geometry("270x400")
root.resizable(width=False, height=False)

#ФУНКЦИИ ДЛЯ ВЫЧЕСЛЕНИЯ

minus = Button(
    text = '-',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command =minus,
    relief = GROOVE
)
minus.place(x=80 , y=320 )

def plus():
    del minus
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a + b)

def minus():
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a - b)

def umno():
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a * b)

def delenie():
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a / b)

def delenie_po_modulu():
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a % b)

def delenie_sleshom():
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a // b)

def vozvedenie_v_stepen():
    global chislo1
    global chislo2
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    b = float(chislo2.get())
    otvet.insert(END, a ** b)

def koren():
    global chislo1
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    otvet.insert(END, math.sqrt(a))

def cos():
    global chislo1
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    otvet.insert(END, math.cos(a))

def sin():
    global chislo1
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    otvet.insert(END, math.sin(a))

def tan():
    global chislo1
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    otvet.insert(END, math.tan(a))

def log():
    global chislo1
    otvet.delete(1.0, END)
    a = float(chislo1.get())
    otvet.insert(END, math.log(a))



#МЕСТА ВВОДА


chislo1 = Entry(
	width=10,
	bg="#b6f774",
	fg='#000000',
	font="Arial 12",
	)
chislo1.place(x=90, y=80)



chislo2 = Entry(
	width=10,
	bg="#b6f774",
	fg='#000000',
	font="Arial 12",
	)
chislo2.place(x=90, y=110)









#КНОПКИ
#ПЕРВАЯ СТРОКА
plus = Button(
    text = '+',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = plus,
    relief = GROOVE
)
plus.place(x=20 , y=320 )







umno = Button(
    text = '*',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command =umno,
    relief = GROOVE
)
umno.place(x=140 , y=320 )



delenie = Button(
    text = '/',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command =delenie,
    relief = GROOVE
)
delenie.place(x=200 , y=320 )


#ВТОРАЯ СТРОКА

del_v2 = Button(
    text = '%',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = delenie_po_modulu,
    relief = GROOVE
)
del_v2.place(x=20 , y=240 )



del_v3 = Button(
    text = '//',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = delenie_sleshom,
    relief = GROOVE
)
del_v3.place(x=80 , y=240 )

stepen = Button(
    text = '^',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = vozvedenie_v_stepen,
    relief = GROOVE
)
stepen.place(x=140 , y=240 )

koren = Button(
    text = '√',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = koren,
    relief = GROOVE
)
koren.place(x=200 , y=240 )

#3 СТРОКА

cos= Button(
    text = 'cos',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = cos,
    relief = GROOVE
)
cos.place(x=20 , y=160 )


sin= Button(
    text = 'sin',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = sin,
    relief = GROOVE
)
sin.place(x=80 , y=160 )



tan= Button(
    text = 'tan',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = tan,
    relief = GROOVE
)
tan.place(x=140 , y=160 )



log= Button(
    text = 'log',
    font = 10,
    bg = '#f0e16d',
    fg = '#000000',
    width = 4,
    height = 2,
    command = log,
    relief = GROOVE
)
log.place(x=200 , y=160 )


#ТЕКСТ С ОТВЕТОМ

otvet = Text(
    width = 20,
    height = 3,
    bg = '#989c9a',
    font = 10
)
otvet.place(relx = 0.10, rely = 0.05, relwidth = 0.8, relheight = 0.13)


plus.focus
root.mainloop()