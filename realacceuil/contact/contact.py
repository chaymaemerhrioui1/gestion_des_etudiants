from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk


def login_page():
    contact.destroy()
    import realacceuil
contact = Tk()
contact.geometry('990x660')
contact.configure(bg='#262626')
contact.resizable(0, 0)
contact.title('Contact')
bg = PhotoImage(file='localisation.png')
label1 = Label(contact, image=bg)
label1.place(x=0,y=0)

l1 = Label(contact, text='Ecole Nationale des Sciences Appliquées d \n'
                         'Al Hoceima BP 03 Ajdir Al hoceima \n '
                         'Tel: +212(0) 539 80 57 12\n'
                         'Fax: +212(0) 539 80 57 13\n ', fg='white', bg='goldenrod2')
l1.config(font=('Arial', 22))
l1.pack(expand=True)
l1.place(x=390,y=70)


loginButton=Button(contact,text='Acceuil',font=('Open Sans','9','bold underline'),bg='white',fg='goldenrod2',bd=0,cursor='hand2',activebackground='white',activeforeground='gold',
                   command=login_page)
loginButton.place(x=20,y=5)

contact.mainloop()