import mysql.connector
import messagebox
from email_verification import send_email_where_id


def forgot_my_id():


    import tkinter as t

    def login():


        try:
            db = mysql.connector.connect(host='localhost', user='root', database='userdata')
            mycursor = db.cursor()
        except mysql.connector.Error:
            messagebox.showerror('Error', 'Data Connectivity Issue. Please Try Again')
            return

        query = 'select id from data where email=%s and password=%s'
        mycursor.execute(query, (email_entry.get(), password_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo(title="ID", message=f'your id is {row}')

    # create a window
    window = t.Tk()
    window.title("capture my ID number")

    # create labels
    email_label = t.Label(text="Email:")
    password_label = t.Label(text="Password:")

    # create entry fields
    email_entry = t.Entry()
    password_entry = t.Entry(show="*")

    # create a login button
    getID = t.Button(text="Login", command=login)

    # add the widgets to the window
    email_label.pack()
    email_entry.pack()
    password_label.pack()
    password_entry.pack()
    getID.pack()

    # run the main event loop
    window.mainloop()