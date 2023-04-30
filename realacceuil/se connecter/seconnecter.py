from tkinter import *
from tkinter import messagebox, simpledialog
import mysql.connector
from PIL import ImageTk
from email_verification import email_verification

def change_password(email):

    import tkinter as tk
    root = tk.Tk()
    root.title("User Authentication Form")
    root.geometry("350x150+100+100")

    # create the form elements

    label_password = tk.Label(root, text="Password")
    label_password.grid(row=3, column=0, padx=10, pady=10)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=3, column=1, padx=10, pady=10)

    label_password_confirm = tk.Label(root, text="Confirm Password")
    label_password_confirm.grid(row=4, column=0, padx=10, pady=10)
    entry_password_confirm = tk.Entry(root, show="*")
    entry_password_confirm.grid(row=4, column=1, padx=10, pady=10)

    button_submit = tk.Button(root, text="Submit", command= lambda: sub_passwrd_change(entry_password, entry_password_confirm, root, email), cursor="hand2")
    button_submit.grid(row=7, column=1, padx=10, pady=10)

    label_error = tk.Label(root, text="")
    label_error.grid(row=8, column=1, padx=10, pady=10)

    # start the main event loop
    root.mainloop()
def sub_passwrd_change(entry_password, entry_password_confirm, root, email):
    if entry_password.get() == '' or entry_password_confirm.get() == '':
        messagebox.showerror('Error', 'All fields are required', parent=root)
    elif entry_password.get() != entry_password_confirm.get():
        messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=root)
    else:
        db = mysql.connector.connect(host='localhost', user='root', database='userdata')
        mycursor = db.cursor()
        query = 'select * from data where email=%s'
        mycursor.execute(query, (email,))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Incorrect email', parent=root)
        else:
            query = 'update data set password=%s where email=%s'
            mycursor.execute(query, (entry_password.get(), email))
            db.commit()
            db.close()
            messagebox.showinfo('Success', 'Password is reset. Please login with new password', parent=root)
            root.destroy()


def login_user():
    if emailEntry.get=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Field are required')
    else:
        try:
            db=mysql.connector.connect(host='localhost',user='root')
            mycursor=db.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)
        #vérifier que le compte existe dans la database
        query='select * from data where email=%s and password=%s'
        mycursor.execute(query,(emailEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid email or password')
        else:
            messagebox.showinfo('Welcome','Login is succeful')


def login_page():
    login_fenetre.destroy()
    import realacceuil
def registr():
    login_fenetre.destroy()
    from registration import registration

def registrement_page():
    login_fenetre.destroy()
    from registration import registration

def on_entry(event):
    if emailEntry.get()=='email':
        emailEntry.delete(0,END)

def pss_entry(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


def hide():  # pour changer masquer a devoiler le mot de passe
    eyeopen.config(file='eyeclose.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    eyeopen.config(file='eyeopen.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    login_fenetre.destroy()
    from signup import signup


def forget_pass():
    user_check= []
    entry = simpledialog.askstring(title="password recapture ",
                                  prompt="enter your email:")

    if '@' not in entry:
        messagebox.showerror('Error',
                             "please use your academic email.")
    if entry.split("@")[1] != "etu.uae.ac.ma":
        messagebox.showerror('Error',
                             "please use your academic email.")

    else:
        email_verification(entry,user_check)
        print("#####")
        print(user_check[0])
        user_input = simpledialog.askstring("input the verification code sent to your email", "code: ")
        user_check.append(user_input)
        # print the user's input
        if user_check[0] == user_check[1]:
            change_password(entry)



#GUI part
login_fenetre=Tk()
login_fenetre.title('Login Page')
login_fenetre.geometry('990x660+50+50')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_fenetre,image=bgImage)
bgLabel.place(x=0,y=0)
heading=Label(login_fenetre,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='#12c4c0')
heading.place(x=600,y=120)


emailEntry=Entry(login_fenetre,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='#12c4c0')
emailEntry.place(x=560,y=200)
emailEntry.insert(0,'email')
emailEntry.bind('<FocusIn>',on_entry)

frame1=Frame(login_fenetre,width=250,height=2,bg='#12c4c0')
frame1.place(x=560,y=222)

#enter your password
passwordEntry=Entry(login_fenetre,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='#12c4c0')
passwordEntry.place(x=560,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pss_entry)
frame2=Frame(login_fenetre,width=250,height=2,bg='#12c4c0')
frame2.place(x=560,y=282)

#masquer ou apparir le mot de passe
eyeopen=PhotoImage(file='eyeopen.png')
eyeButton=Button(login_fenetre,image=eyeopen,bd=0,bg='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

#mot de passe oublier
forgetButton=Button(login_fenetre,text='mot de passe oublié',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',8,'bold'),fg='#12c4c0', command=forget_pass)

forgetButton.place(x=715,y=295)


#loggin button
loginButton=Button(login_fenetre,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='#12c4c0',activebackground='white',activeforeground='white',cursor='hand2',bd=0,width=19, command= login_user)
loginButton.place(x=578,y=350)

#gmail button
google_logo=PhotoImage(file='googlech.png')
google_logolabel=Label(login_fenetre,image=google_logo,bg='white')
google_logolabel.place(x=680,y=440)

#sign up label
signupLabel=Label(login_fenetre,text='inscrivez-vous',font=('Open Sans',8,'bold'),fg='#12c4c0',bg='white' )
signupLabel.place(x=598,y=500)
newaccountButton=Button(login_fenetre,text='Creer un nouveau compte',font=('Open Sans',8,'bold underline'),bd=0,fg='blue',bg='white',activebackground='white',activeforeground='blue',cursor='hand2',
                        command=signup_page)
newaccountButton.place(x=700,y=500)


#acceuil button pour retourner
loginButton=Button(frame2,text='Acceuil',font=('Open Sans','9','bold underline'),bg='white',fg='#12c4c0',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',
                   command=login_page)
loginButton.place(x=690,y=430)


loginButton=Button(login_fenetre,text='Menu',font=('Open Sans','9','bold underline'),bg='white',fg='#12c4c0',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',
                   command=login_page)
loginButton.place(x=15,y=49)




login_fenetre.mainloop()