from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk

def login_user():
    if usernameEntry.get=='' or passwordEntry.get()=='':
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
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is succeful')


def login_page():
    login_fenetre.destroy()
    import realacceuil
def registr():
    login_fenetre.destroy()
    import registration

def registrement_page():
    login_fenetre.destroy()
    import registration

def on_entry(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

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
    import signup


def forget_pass():
    def change_password():
        if user_entry.get() == '' or confirmpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=window)
        elif password_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=window)
        else:
            db = mysql.connector.connect(host='localhost', user='root', database='userdata')
            mycursor = db.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get(),))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (confirmpass_entry.get(), user_entry.get()))
                db.commit()
                db.close()
                messagebox.showinfo('Success', 'Password is reset. Please login with new password', parent=window)
                window.destroy()


    window= Toplevel()
    window.title('Change Password')
    bgPic=ImageTk.PhotoImage(file='background.jpg')
    bglabel=Label(window,image=bgPic)
    bglabel.grid()
    heading_label=Label(window,text='RESET PASSWORD',font=('arial',16,'bold'),bg='white',fg='magenta2')
    heading_label.place(x=480,y=60)

    #user
    userLabel=Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='orchid1')
    userLabel.place(x=470,y=130)

    user_entry=Entry(window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    user_entry.place(x=470,y=160)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)
    #newpassword
    passwordLabel =Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white',fg='orchid1')
    passwordLabel.place(x=470, y=210)

    password_entry=Entry(window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    password_entry.place(x=470,y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpassLabel=Label(window, text='Confirm Password', font=('arial', 12, 'bold'),bg='white',fg='orchid1')
    confirmpassLabel.place(x=470, y=290)
    confirmpass_entry=Entry(window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    confirmpass_entry.place(x=470,y=320)
    emaillabel = Label(window, text='Email', font=('arial', 10, 'bold'), bg='white', fg='orchid1')
    emaillabel.place(x=470,y=340)
    emailEntry = Entry(window, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
    emailEntry.grid(row=2, column=0, sticky='w', padx=25)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)
    SubmitButton = Button(window, text='Submit', font=('Open Sans', 16, 'bold'), fg='white', bg='magenta2',
                          activebackground='magenta2', activeforeground='white', cursor='hand2', bd=0, width=19,
                          command=change_password)
    SubmitButton.place(x=470, y=390)

    window.mainloop()





#GUI part
login_fenetre=Tk()
login_fenetre.title('Login Page')
login_fenetre.geometry('990x660+50+50')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_fenetre,image=bgImage)
bgLabel.place(x=0,y=0)
heading=Label(login_fenetre,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='#12c4c0')
heading.place(x=600,y=120)


usernameEntry=Entry(login_fenetre,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='#12c4c0')
usernameEntry.place(x=560,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_entry)

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
forgetButton=Button(login_fenetre,text='mot de passe oublié',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',8,'bold'),fg='#12c4c0')

forgetButton.place(x=715,y=295)


#loggin button
loginButton=Button(login_fenetre,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='#12c4c0',activebackground='white',activeforeground='white',cursor='hand2',bd=0,width=19)
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