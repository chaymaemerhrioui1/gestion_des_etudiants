
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector



def clear():
    emailEntry.delete(0, END)
    first_nameEntry.delete(0, END)
    last_nameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)


def login_page():
    signup_fenetre.destroy()
    import seconnecter

def registrement_page():
    signup_fenetre.destroy()
    import registration

def connect_database():
    if emailEntry.get() == '' or first_nameEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    elif emailEntry.get().split("@")[1] != "etu.uae.ac.ma":
        messagebox.showerror('Error', "please use your academic email.\n if you don't have one or if the one you have doesn't bellong to Abdelmalek Assaadi's university(@etu.uae.ac.ma), then we are afraid you cannot create an accout")

    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root')
            mycursor = db.cursor()
        except mysql.connector.Error:
            messagebox.showerror('Error', 'Data Connectivity Issue. Please Try Again')
            return
        try:
            query = 'CREATE DATABASE IF NOT EXISTS userdata'
            mycursor.execute(query)
            query = 'USE userdata'
            mycursor.execute(query)
            query = 'CREATE TABLE IF NOT EXISTS data(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, email VARCHAR(50), first_name VARCHAR(100), last_name VARCHAR(100), password VARCHAR(50))'
            mycursor.execute(query)
        except mysql.connector.Error:
            mycursor.execute('USE userdata')


        query = 'SELECT * FROM data WHERE email=%s'
        mycursor.execute(query, (emailEntry.get(),))

        # Vérifier que l'utilisateur existe déjà
        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already Exists')
        else:
            query = 'INSERT INTO data(email, first_name,last_name, password) VALUES (%s, %s, %s, %s)'
            values = (emailEntry.get(), first_nameEntry.get(), last_nameEntry.get(), passwordEntry.get())
            mycursor.execute(query, values)
            db.commit()
            db.close()
            messagebox.showinfo('Success', 'Registration Successful')
            clear()



signup_fenetre = Tk()
signup_fenetre.resizable(False, False)
background = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(signup_fenetre, image=background)
bgLabel.grid()

frame = Frame(signup_fenetre, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='Creer un compte', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                    fg='#12c4c0')
heading.grid(row=0, column=0, padx=15, sticky='w')

    # email
emaillabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='#12c4c0')
emaillabel.grid(row=1, column=0, sticky='w', padx=25)
emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#12c4c0', fg='white')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

    # first_name
first_namelabel = Label(frame, text="Prenom d'Utilisateur", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='#12c4c0')
first_namelabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
first_nameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#12c4c0', fg='white')
first_nameEntry.grid(row=4, column=0, sticky='w', padx=25)

last_namelabel = Label(frame, text="Nom d'Utilisateur", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='#12c4c0')
last_namelabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
last_nameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#12c4c0', fg='white')
last_nameEntry.grid(row=6, column=0, sticky='w', padx=25)

    # mot de passe
passwordlabel = Label(frame, text='Mot de passe', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='#12c4c0')
passwordlabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='#12c4c0',fg='white')
passwordEntry.grid(row=8,column=0,sticky='w',padx=25)
#confirmer mot de passe
confirmpasswordlabel=Label(frame,text='Confirmer mot de passe',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#12c4c0')
confirmpasswordlabel.grid(row=9,column=0,sticky='w',padx=25,pady=(10,0))
confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='#12c4c0',fg='white')
confirmpasswordEntry.grid(row=10,column=0,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='j accepte les termes et les conditions',font=('Microsoft Yahei UI Light',10,'bold'),fg='#12c4c0',bg='white',activebackground='white',activeforeground='#12c4c0',cursor='hand2',
                               variable=check)
termsandconditions.grid(row=11,column=0,pady=10,padx=15)

#le boutton s'inscrire
signupButton=Button(frame,text='s inscrire',font=('Microsoft Yahei UI Light',10,'bold'),bd=0,bg='#12c4c0',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=12,column=0,pady=10)

alreadyaccount=Label(frame, text='Voulez- vous continuer l inscription ?',font=('Open Sans','9','bold'),bg='white',fg='#12c4c0')
alreadyaccount.grid(row=13,column=0,sticky='w',padx=25,pady=30)

#loginButton=Button(frame,text='Se connecter',font=('Open Sans','9','bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',
                  # command=login_page)
#loginButton.place(x=170,y=397)

loginButton=Button(frame,text='Oui',font=('Open Sans','9','bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',
                   command=registrement_page)
loginButton.place(x=250,y=397)


signup_fenetre.mainloop()