from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk

win = Tk()
win.title("Privet")
win.geometry('600x600')

def control():
    accept()
    picture()

def accept():
    show.config(text=spisok.get(ANCHOR))
    print(spisok.get(ANCHOR))
    if spisok.get(ANCHOR) == 'Наруто Узумаки':
        txt.delete(1.0, END)
        f = open('naruto.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Сакура Харуно':
        txt.delete(1.0, END)
        f = open('Sakura.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Саске Учиха':
        txt.delete(1.0, END)
        f = open('Saske.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Какаши Хатаке':
        txt.delete(1.0, END)
        f = open('Kakashi.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    

def picture():
    global a
    a = ""
    show.config(text=spisok.get(ANCHOR))
    if spisok.get(ANCHOR) == "Наруто Узумаки":
        a = ImageTk.PhotoImage(Image.open('img/naruto.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Сакура Харуно':
        a = ImageTk.PhotoImage(Image.open('img/Sakura.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Саске Учиха':
        a = ImageTk.PhotoImage(Image.open('img/Saske.gif'))
        b = Label(win, image=a, width=1000, height=500, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Какаши Хатаке':
        a = ImageTk.PhotoImage(Image.open('img/Kakashi.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
   

spisok = Listbox(selectmode=SINGLE, width=10, height=12)
spisok.insert(0, 'Наруто Узумаки')
spisok.insert(1, 'Сакура Харуно')
spisok.insert(2, 'Саске Учиха')
spisok.insert(3, 'Какаши Хатаке')
spisok.grid(column=0, row=0, padx=10)

Button(win, text='Подтвердить', command=control).grid(column=1, row=0)

txt = scrolledtext.ScrolledText(win, width=40, height=10, borderwidth=5)
txt.grid(column=2, row=0, padx=10)

show = Label(win)
win.mainloop()
