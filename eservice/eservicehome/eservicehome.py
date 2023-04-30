from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

def cour_page():
    w.destroy()
    import cours

def eservice():
    w.destroy()
    import seconnecter

def carte_page():
    w.destroy()
    import carte

def marksheet_page():
    w.destroy()
    import marksheet

def eservicehome_page():
    w.destroy()
    import cours

def clubs_page():
    w.destroy()
    import Clubs

w = Tk()
w.geometry('990x660')
w.configure(bg='#262626')
w.resizable(0, 0)
w.title(' My Eservice')
bg = PhotoImage(file="pexels-pixaby.png")
label1 = Label(w, image=bg)
label1.place(x=0,y=0)

l1 = Label(w, text='Bienvenue  !\n'
                   'Espace Etudiants de l ecole Nationale \n'
                   'des sciences appliquée Al hoceima ', fg='white', bg='#262626')
l1.config(font=('Arial', 30))
l1.pack(expand=True)
l1.place(x=200,y=250)


def toggle_win():
    f1 = Frame(w, width=230, height=700, bg='white')
    f1.place(x=0, y=0)

    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,width=30,height=2,fg='#262626',
                           border=0,bg=fcolor,activeforeground='#262626',
                           activebackground=bcolor,command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)



    options_frame = tk.Frame(w, bg='white')



    bttn(0, 100, 'COURS', 'grey', 'white',cour_page)
    bttn(0, 150, 'CARTE ETUDIANT', 'grey', 'white', carte_page)
    bttn(0, 200, 'MARKSHEET', 'grey', 'white', marksheet_page)
    bttn(0, 250, 'Clubs', 'grey', 'white', clubs_page)

    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close-button (1).png"))

    Button(f1,image=img2,border=0,command=dele,bg='white',
           activebackground='white').place(x=5, y=10)

img1 = ImageTk.PhotoImage(Image.open("menu (1).png"))
Button(w, image=img1,command=toggle_win,border=0,bg='#262626',
       activebackground='#262626').place(x=5, y=10)

w.mainloop()