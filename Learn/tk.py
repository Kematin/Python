#Tkinter
from tkinter import *



root = Tk()
root['bg'] = '#808080' #цвет заднего фона
root.title('лохотрон 2000') #название
#root.wm_attributes('-alpha', 0,8) #прозрачность
root.geometry('300x250') #рамеры окна
root.resizable(width=False, height=False) #Разрешение изменения размеров окна

def bk():
	login = loginInput.get()
	password = passField.get()

	info_str = f'Данные: {str(login)}, {str(password)}'
	messagebox.showinfo(title = "Информация", message = info_str)

	#messagebox.showerror(title = '', message = 'ERROR')


canvas = Canvas(root, height = 150, width = 125) # что-то вроде холста для рисования
canvas.pack()




frame = Frame(root, bg='#4cbded')        #Какое либо место в программе
frame.place(relx = 0.10, rely = 0.10, relwidth = 0.8, relheight = 0.8)




title = Label(frame, 
	text = 'Подсказка', 
	bg ='#b1b3b1', 
	font = 10) 
title.pack()
'''текст который нельзя изменить'''



btn1 = Button(frame,
	text = "Ты лох",
	bg = 'Yellow',
	font = 10,
	command = bk)
btn1.pack()




root.mainloop()

