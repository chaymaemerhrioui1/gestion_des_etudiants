from tkinter import *  # importing all the modules and widgets from tkinter
from tkinter import messagebox as mb  # importing the messagebox module from tkinter

import messagebox
import mysql.connector
from PIL import ImageTk, Image, ImageDraw, \
ImageFont  # importing the ImageTk, Image, ImageDraw and ImageFont modules from PIL

#fct
def marksheet_page():
    gui_root.destroy()
#   import eservicehome

# defining a function to calculate the total





def calculate_total(sub1, sub2, sub3, sub4, sub5):
    # adding all the arguments
    total = sub1 + sub2 + sub3 + sub4 + sub5
    # returning the total
    return total




# defining a function to calculate the percentage
def calculate_percentage(total):
    # dividing the total by number of subjects (5)
    percentage = total / 5
    # returning the percentage
    return percentage


# defining a function to calculate the grade
def calculate_grade(percentage):
    if (percentage >= 18.0):
        return 'excellent '
    elif (percentage >= 16.0 and percentage < 18.0):
        return 'Mention Très bien '
    elif (percentage >= 14.0 and percentage < 16.0):
        return 'Mention Bien '
    elif (percentage >= 12.0 and percentage < 14.0):
        return 'Passable '
    elif (percentage >= 10.0 and percentage < 12.0):
        return 'Passable'
    else:
        return 'pas réussi cette année'

    # defining a function to calculate the result


def calculate_result(percentage, sub1, sub2, sub3, sub4, sub5):
    # using if-else conditional statement to whether the student is pass or fail
    if (percentage >= 6.6 and sub1 >= 6.6 and sub2 >= 6.6 and sub3 >= 6.6 and sub4 >= 6.6 and sub5 >= 6.6):
        return 'PASS'
    else:
        return 'FAIL'

    # defining a function to check the errors


def check_for_errors():
    # using if conditional statement to check if the entries are invalid
    if (
            marks_One_field.get() == "" or marks_Two_field == "" or marks_Three_field == "" or marks_Four_field == "" or marks_Five_field == ""):
        # displaying the message box with the error message
        mb.showerror("Invalid Input", "Marks must be in float data type.")

        # calling the function to reset entries
        reset_subject_entries()

        # returning -1
        return -1

    # defining a function to display the result


def insert_notes(marks1, marks2, marks3, marks4, marks5, num_id):
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
        query = 'CREATE DATABASE IF NOT EXISTS userdata'
        mycursor.execute(query)
        query = 'USE userdata'
        mycursor.execute(query)
        query = ("""
                    CREATE TABLE IF NOT EXISTS notes (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        note1 FLOAT NOT NULL,
                        note2 FLOAT NOT NULL,
                        note3 FLOAT NOT NULL,
                        note4 FLOAT NOT NULL,
                        note5 FLOAT NOT NULL,
                        data_id INT NOT NULL,
                        FOREIGN KEY (data_id) REFERENCES data(id)
                    )
                """)
        mycursor.execute(query)
    except mysql.connector.Error:
        mycursor.execute('USE userdata')

    try:
        mycursor.execute("""
            INSERT INTO notes (note1, note2, note3, note4, note5, data_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (marks1, marks2, marks3, marks4, marks5, num_id))

        # Commit the changes to the database
        db.commit()

        # Print the number of rows affected by the query
        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error:
        messagebox.showerror('error', 'failed to execute the query')


def save_results(total, percentage, grade, result, id):
    try:
        db = mysql.connector.connect(host='localhost', user='root')
        mycursor = db.cursor()
    except mysql.connector.Error:
        messagebox.showerror('Error', 'Data Connectivity Issue. Please Try Again')
        return

    try:
        query = ("""CREATE TABLE IF NOT EXISTS results (
            id INT PRIMARY KEY AUTO_INCREMENT,
            total FLOAT(5),
            percentage FLOAT(5),
            grade VARCHAR(10), 
            result VARCHAR(25),
            FOREIGN KEY (data_id) REFERENCES data(id)
            )""")
        mycursor.execute(query)
    except mysql.connector.Error:
        mycursor.execute('USE userdata')
        print('fail')

    try:
        mycursor.execute("""
            INSERT INTO resultS (total, percentage, grade,result, data_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (total, percentage, grade, result, id))

        # Commit the changes to the database
        db.commit()

        # Print the number of rows affected by the query
        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error:
        messagebox.showerror('error', 'failed to execute the query')


def display_result():
    # using the get() method to get subject names
    sub1 = subject_One_field.get()
    sub2 = subject_Two_field.get()
    sub3 = subject_Three_field.get()
    sub4 = subject_Four_field.get()
    sub5 = subject_Five_field.get()

    # checking if the strings are empty or not
    if (sub1 == "" and sub2 == "" and sub3 == "" and sub4 == "" and sub5 == ""):
        # displaying the message box with the error message
        mb.showerror("Empty Fields", "Subject fields cannot be empty.")

        # calling the function to reset entries
        reset_subject_entries()
    else:
        # calling the check_for_errors() function and storing the value
        val = check_for_errors()

        # if the stored value is -1, then return
        if val == -1:
            return
        else:
            # using the get() method to get the marks and converting them into float
            marks1 = float(marks_One_field.get())
            marks2 = float(marks_Two_field.get())
            marks3 = float(marks_Three_field.get())
            marks4 = float(marks_Four_field.get())
            marks5 = float(marks_Five_field.get())


            # using the if-else conditional statement to check if the marks entered are valid and ranging in between 0 to 100
            if (
                    marks1 >= 0 and marks1 <= 20 and marks2 >= 0 and marks2 <= 20 and marks3 >= 0 and marks3 <= 20 and marks4 >= 0 and marks4 <= 20 and marks5 >= 0 and marks5 <= 20):
                insert_notes(marks1,marks2,marks3,marks4,marks5,regd_num_field.get())
                # calculating the result by calling the functions we created earlier and storing their values
                total = calculate_total(marks1, marks2, marks3, marks4, marks5)
                percentage = calculate_percentage(total)
                grade = calculate_grade(percentage)
                result = calculate_result(percentage, marks1, marks2, marks3, marks4, marks5)

                save_results(total,percentage,grade,result, regd_num_field.get())
                # setting the grade to 'F', if the result is 'FAIL'
                if result == 'FAIL':
                    grade = 'F'

                    # calling the function to disable the entry fields
                disable_field()

                # configuring the labels displaying result by setting their text to the corresponding values
                display_total_label.config(text=total)
                display_percentage_label.config(text=percentage)
                display_grade_label.config(text=grade)
                display_result_label.config(text=result)

                # configuring the state of the 'Generate Marksheet' button to normal
                generate_button.config(state="normal")
            else:
                # displaying message box with error message
                mb.showerror("Out of Range", "Marks must be ranging between 0 to 20.")

                # calling the function to reset the entries
                reset_subject_entries()

            # defining a function to generate marksheet as a PNG file


def generate_marksheet():
    # using the get() method to get the entries from the entry field
    # student's information
    student_name = str(name_field.get())
    student_dob = str(dob_field.get())
    student_class = str(class_field.get())
    regd_num = str(regd_num_field.get())
    school_name = str(school_field.get())
    roll_num = str(roll_num_field.get())

    # names of the subjects
    sub1 = str(subject_One_field.get())
    sub2 = str(subject_Two_field.get())
    sub3 = str(subject_Three_field.get())
    sub4 = str(subject_Four_field.get())
    sub5 = str(subject_Five_field.get())

    # marks of the subjects
    marks1 = str(marks_One_field.get())
    marks2 = str(marks_Two_field.get())
    marks3 = str(marks_Three_field.get())
    marks4 = str(marks_Four_field.get())
    marks5 = str(marks_Five_field.get())

    # using cget() method to retrieve text from the result labels
    total = str(display_total_label.cget("text"))
    percentage = str(display_percentage_label.cget("text"))
    grade = str(display_grade_label.cget("text"))
    result = str(display_result_label.cget("text"))

    # importing the image of a report card using
    # the open() method of the Image module
    report_card_img = Image.open("C://Users//Salma Fannich//Downloads//REPORT-CARD_1.png")
    # using the Draw() class of the ImageDraw module
    # to make 2D drawing interface
    draw_obj = ImageDraw.Draw(report_card_img)

    # defining coordinates
    point1 = 380, 200
    point2 = 480, 385
    point3 = 480, 440
    point4 = 480, 495
    point5 = 480, 550
    point6 = 480, 605
    point7 = 420, 900
    point8 = 1100, 900
    point9 = 420, 966.6
    point10 = 1100, 966.6
    point11 = 420, 1032.3
    point12 = 1100, 1032.3
    point13 = 420, 1100
    point14 = 1100, 1100
    point15 = 420, 1166.6
    point16 = 1100, 1166.6
    point17 = 700, 1380
    point18 = 700, 1450
    point19 = 700, 1520
    point20 = 700, 1680

    # specifying the fonts for the text
    fontOne = ImageFont.truetype("verdana.ttf", 70)
    fontTwo = ImageFont.truetype("verdana.ttf", 40)
    fontThree = ImageFont.truetype("verdana.ttf", 50)

    # adding text values to the image
    draw_obj.text(point1, school_name, "black", font=fontOne)
    draw_obj.text(point2, regd_num, "black", font=fontTwo)
    draw_obj.text(point3, roll_num, "black", font=fontTwo)
    draw_obj.text(point4, student_name, "black", font=fontTwo)
    draw_obj.text(point5, student_dob, "black", font=fontTwo)
    draw_obj.text(point6, student_class, "black", font=fontTwo)
    draw_obj.text(point7, sub1, "black", font=fontTwo)
    draw_obj.text(point8, marks1, "black", font=fontTwo)
    draw_obj.text(point9, sub2, "black", font=fontTwo)
    draw_obj.text(point10, marks2, "black", font=fontTwo)
    draw_obj.text(point11, sub3, "black", font=fontTwo)
    draw_obj.text(point12, marks3, "black", font=fontTwo)
    draw_obj.text(point13, sub4, "black", font=fontTwo)
    draw_obj.text(point14, marks4, "black", font=fontTwo)
    draw_obj.text(point15, sub5, "black", font=fontTwo)
    draw_obj.text(point16, marks5, "black", font=fontTwo)
    draw_obj.text(point17, total, "black", font=fontTwo)
    draw_obj.text(point18, percentage, "black", font=fontTwo)
    draw_obj.text(point19, grade, "black", font=fontTwo)
    draw_obj.text(point20, result, "black", font=fontThree)

    # saving the image file
    report_card_img.save(rf'{name_field.get()}.png')

    # displaying the image
    report_card_img.show()


# defining a function to disable the fields
def disable_field():
    # disabling all the entry fields by using the config()
    # method and setting the state parameter to 'disabled'
    name_field.config(state="disabled")
    dob_field.config(state="disabled")
    class_field.config(state="disabled")
    regd_num_field.config(state="disabled")
    school_field.config(state="disabled")
    roll_num_field.config(state="disabled")
    subject_One_field.config(state="disabled")
    subject_Two_field.config(state="disabled")
    subject_Three_field.config(state="disabled")
    subject_Four_field.config(state="disabled")
    subject_Five_field.config(state="disabled")
    marks_One_field.config(state="disabled")
    marks_Two_field.config(state="disabled")
    marks_Three_field.config(state="disabled")
    marks_Four_field.config(state="disabled")
    marks_Five_field.config(state="disabled")
    result_button.config(state="disabled")


# defining a function to enable the fields
def enable_field():
    # enabling all the entry fields by using the config()
    # method and setting the state parameter to 'normal'
    name_field.config(state="normal")
    dob_field.config(state="normal")
    class_field.config(state="normal")
    regd_num_field.config(state="normal")
    school_field.config(state="normal")
    roll_num_field.config(state="normal")
    subject_One_field.config(state="normal")
    subject_Two_field.config(state="normal")
    subject_Three_field.config(state="normal")
    subject_Four_field.config(state="normal")
    subject_Five_field.config(state="normal")
    marks_One_field.config(state="normal")
    marks_Two_field.config(state="normal")
    marks_Three_field.config(state="normal")
    marks_Four_field.config(state="normal")
    marks_Five_field.config(state="normal")
    result_button.config(state="normal")


# defining a function to reset entries in the subject's information columns
def reset_subject_entries():
    # calling the enable_field() function we defined earlier
    enable_field()

    # deleting the entries in the field using the delete() method
    subject_One_field.delete(0, END)
    subject_Two_field.delete(0, END)
    subject_Three_field.delete(0, END)
    subject_Four_field.delete(0, END)
    subject_Five_field.delete(0, END)
    marks_One_field.delete(0, END)
    marks_Two_field.delete(0, END)
    marks_Three_field.delete(0, END)
    marks_Four_field.delete(0, END)
    marks_Five_field.delete(0, END)

    # setting the focus to first subject field using the focus_set() method
    subject_One_field.focus_set()


# defining a function to clear all entries
def reset():
    # calling the reset_subject_entries() method we defined earlier
    reset_subject_entries()

    # deleting the entries of the fields in the student's information columns
    name_field.delete(0, END)
    dob_field.delete(0, END)
    class_field.delete(0, END)
    regd_num_field.delete(0, END)
    school_field.delete(0, END)
    roll_num_field.delete(0, END)

    # configuring the initial text of the labels
    display_total_label.config(text="0")
    display_percentage_label.config(text="0")
    display_grade_label.config(text="XXXX")
    display_result_label.config(text="XXXX")

    # disabling the 'Generate Marksheet' button
    generate_button.config(state="disabled")

    # setting the focus to name field using the focus_set() method
    name_field.focus_set()


# defining a function to exit the application
def exit():
    # using the destroy() method to close the application
    gui_root.destroy()


# main function
if __name__ == "__main__":
    # main window
    # creating an object of the Tk() class
    gui_root = Tk()

    # setting the title of the application
    gui_root.title("Marksheet Generator")

    # setting the size and position of the application
    gui_root.geometry("800x700+650+200")

    # disabling the resizable option
    gui_root.resizable(0, 0)

    # configuring the background color of the application to #FCEEF6
    gui_root.config(bg="#FCEEF6")

    # setting the icon of the application
    gui_root.iconbitmap("close.png")

    # defining frames to provide structure to other widgets
    header_frame = Frame(gui_root, bg="#B05D8D")
    heading_frame = Frame(header_frame, bg="#B05D8D")
    subheading_frame = Frame(header_frame, bg="#5C153E")
    info_frame = Frame(gui_root, bg="#FCEEF6")
    subject_frame = Frame(gui_root, bg="#FCEEF6")
    result_frame = Frame(gui_root, bg="#FCEEF6")
    buttons_frame = Frame(gui_root, bg="#FCEEF6")

    # using the pack() method to set the positions of these frames
    header_frame.pack(fill="both")
    heading_frame.pack()
    subheading_frame.pack(fill="both")
    info_frame.pack()
    subject_frame.pack()
    result_frame.pack(pady=15)
    buttons_frame.pack()

    # ---------------------- The heading_frame Frame ----------------------
    # importing an image
    the_image = ImageTk.PhotoImage(Image.open("close.png").resize((50, 50), Image.ANTIALIAS))

    # adding some labels to display an image and heading of the application
    image_label = Label(heading_frame, image=the_image, bg="#B05D8D")
    header_label = Label(heading_frame, text="Marksheet", font=("verdana", "24", "bold"), bg="#B05D8D", fg="#FFFFFF")

    # using the grid() method to set the positions of these labels in a grid format
    image_label.grid(row=0, column=0, padx=2.5, pady=5)
    header_label.grid(row=0, column=1, padx=2.5, pady=5)

    # ---------------------- The subheading_frame Frame ----------------------
    # adding a label to display sub-heading of the application
    subheader_label = Label(subheading_frame, text="Create your own Marksheet", font=("verdana", "10"), bg="#5C153E",
                            fg="#FEB9E1")

    # using the pack() method to set the position of this label
    subheader_label.pack(pady=5)

    # ---------------------- The info_frame Frame ----------------------
    # defining some labels to display text asking user to enter details
    info_label = Label(info_frame, text="Student's Information", font=("Times New Roman", "12", "bold"), bg="#FCEEF6",
                       fg="#5C153E")
    name_label = Label(info_frame, text="Name of the Student:", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                       fg="#B05D8D")
    dob_label = Label(info_frame, text="Date of Birth:", bg="#FCEEF6", font=("Times New Roman", "11", "bold"),
                      fg="#B05D8D")
    class_label = Label(info_frame, text="Programme/Class:", bg="#FCEEF6", font=("Times New Roman", "11", "bold"),
                        fg="#B05D8D")
    regd_num_label = Label(info_frame, text="Registration Number:", font=("Times New Roman", "11", "bold"),
                           bg="#FCEEF6", fg="#B05D8D")
    school_label = Label(info_frame, text="Name of the Institution:", font=("Times New Roman", "11", "bold"),
                         bg="#FCEEF6", fg="#B05D8D")
    roll_num_label = Label(info_frame, text="Roll Number:", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                           fg="#B05D8D")

    # using the grid() method to set the positions of these labels in a grid format
    info_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    dob_label.grid(row=1, column=2, padx=5, pady=5, sticky=E)
    class_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    regd_num_label.grid(row=2, column=2, padx=5, pady=5, sticky=E)
    school_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    roll_num_label.grid(row=3, column=2, padx=5, pady=5, sticky=E)

    # defining some entry fields for the user to enter the asked details
    name_field = Entry(info_frame, width=25, font=("Times New Roman", "11"), bg="#FFFFFF", fg="#5C153E", relief=GROOVE)
    dob_field = Entry(info_frame, width=10, font=("Times New Roman", "11"), bg="#FFFFFF", fg="#5C153E", relief=GROOVE)
    class_field = Entry(info_frame, width=25, font=("Times New Roman", "11"), bg="#FFFFFF", fg="#5C153E", relief=GROOVE)
    regd_num_field = Entry(info_frame, width=10, font=("Times New Roman", "11"), bg="#FFFFFF", fg="#5C153E",
                           relief=GROOVE)
    school_field = Entry(info_frame, width=25, font=("Times New Roman", "11"), bg="#FFFFFF", fg="#5C153E",
                         relief=GROOVE)
    roll_num_field = Entry(info_frame, width=10, font=("Times New Roman", "11"), bg="#FFFFFF", fg="#5C153E",
                           relief=GROOVE)

    # using the grid() method to set the positions of these fields in a grid format
    name_field.grid(row=1, column=1, padx=5, pady=5)
    dob_field.grid(row=1, column=3, padx=5, pady=5)
    class_field.grid(row=2, column=1, padx=5, pady=5)
    regd_num_field.grid(row=2, column=3, padx=5, pady=5)
    school_field.grid(row=3, column=1, padx=5, pady=5)
    roll_num_field.grid(row=3, column=3, padx=5, pady=5)

    # ---------------------- The subject_frame Frame ----------------------
    # defining some labels to display text asking user to enter their subject's information
    subjects_label = Label(subject_frame, text="Subjects Information", font=("Times New Roman", "12", "bold"),
                           bg="#FCEEF6", fg="#5C153E")
    subject_name_label = Label(subject_frame, text="Subject Name", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                               fg="#5C153E")
    marks_label = Label(subject_frame, text="Marks Obtained", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                        fg="#5C153E")
    marks_extra_label = Label(subject_frame, text="(Out of 20)", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                              fg="#5C153E")
    subject_One_label = Label(subject_frame, text="Subject I :", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                              fg="#B05D8D")
    subject_Two_label = Label(subject_frame, text="Subject II :", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                              fg="#B05D8D")
    subject_Three_label = Label(subject_frame, text="Subject III :", font=("Times New Roman", "11", "bold"),
                                bg="#FCEEF6", fg="#B05D8D")
    subject_Four_label = Label(subject_frame, text="Subject IV :", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                               fg="#B05D8D")
    subject_Five_label = Label(subject_frame, text="Subject V :", font=("Times New Roman", "11", "bold"), bg="#FCEEF6",
                               fg="#B05D8D")

    # using the grid() method to set the position of these labels in a grid format
    subjects_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
    subject_name_label.grid(row=1, column=1, padx=5)
    marks_label.grid(row=1, column=2, padx=5)
    marks_extra_label.grid(row=2, column=2, padx=5, pady=2.5)
    subject_One_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    subject_Two_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    subject_Three_label.grid(row=5, column=0, padx=5, pady=5, sticky=E)
    subject_Four_label.grid(row=6, column=0, padx=5, pady=5, sticky=E)
    subject_Five_label.grid(row=7, column=0, padx=5, pady=5, sticky=E)

    # defining some entry fields for the users to enter the asked details
    subject_One_field = Entry(subject_frame, width=30, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                              fg="#5C153E", relief=GROOVE)
    marks_One_field = Entry(subject_frame, width=5, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                            fg="#5C153E", relief=GROOVE)
    subject_Two_field = Entry(subject_frame, width=30, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                              fg="#5C153E", relief=GROOVE)
    marks_Two_field = Entry(subject_frame, width=5, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                            fg="#5C153E", relief=GROOVE)
    subject_Three_field = Entry(subject_frame, width=30, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                                fg="#5C153E", relief=GROOVE)
    marks_Three_field = Entry(subject_frame, width=5, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                              fg="#5C153E", relief=GROOVE)
    subject_Four_field = Entry(subject_frame, width=30, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                               fg="#5C153E", relief=GROOVE)
    marks_Four_field = Entry(subject_frame, width=5, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                             fg="#5C153E", relief=GROOVE)
    subject_Five_field = Entry(subject_frame, width=30, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                               fg="#5C153E", relief=GROOVE)
    marks_Five_field = Entry(subject_frame, width=5, font=("Times New Roman", "11"), justify=CENTER, bg="#FFFFFF",
                             fg="#5C153E", relief=GROOVE)

    # using the grid() method to set the positions of these fields in a grid format
    subject_One_field.grid(row=3, column=1, padx=5, pady=5)
    marks_One_field.grid(row=3, column=2, padx=5, pady=5)
    subject_Two_field.grid(row=4, column=1, padx=5, pady=5)
    marks_Two_field.grid(row=4, column=2, padx=5, pady=5)
    subject_Three_field.grid(row=5, column=1, padx=5, pady=5)
    marks_Three_field.grid(row=5, column=2, padx=5, pady=5)
    subject_Four_field.grid(row=6, column=1, padx=5, pady=5)
    marks_Four_field.grid(row=6, column=2, padx=5, pady=5)
    subject_Five_field.grid(row=7, column=1, padx=5, pady=5)
    marks_Five_field.grid(row=7, column=2, padx=5, pady=5)

    # ---------------------- The result_frame Frame ----------------------
    # defining some labels to display the result
    total_label = Label(result_frame, text="Total:", font=("Times New Roman", "12", "bold"), bg="#FCEEF6", fg="#5C153E")
    display_total_label = Label(result_frame, text="0", font=("Times New Roman", "12"), bg="#FCEEF6", fg="#5C153E")
    percentage_label = Label(result_frame, text="Percentage (%):", font=("Times New Roman", "12", "bold"), bg="#FCEEF6",
                             fg="#5C153E")
    display_percentage_label = Label(result_frame, text="0", font=("Times New Roman", "12"), bg="#FCEEF6", fg="#5C153E")
    grade_label = Label(result_frame, text="Grade:", font=("Times New Roman", "12", "bold"), bg="#FCEEF6", fg="#5C153E")
    display_grade_label = Label(result_frame, text="XXXX", font=("Times New Roman", "12"), bg="#FCEEF6", fg="#5C153E")
    result_label = Label(result_frame, text="Result:", font=("Times New Roman", "12", "bold"), bg="#FCEEF6",
                         fg="#5C153E")
    display_result_label = Label(result_frame, text="XXXX", font=("Times New Roman", "14", "bold"), bg="#FCEEF6",
                                 fg="#5C153E")

    # using the grid() method to set the positions of these labels in a grid format
    total_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    display_total_label.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    percentage_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    display_percentage_label.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    grade_label.grid(row=0, column=4, padx=5, pady=5, sticky=W)
    display_grade_label.grid(row=0, column=5, padx=5, pady=5, sticky=W)
    result_label.grid(row=0, column=6, padx=5, pady=5, sticky=W)
    display_result_label.grid(row=0, column=7, padx=5, pady=5, sticky=W)

    # ---------------------- The buttons_frame Frame ----------------------
    # defining some buttons to manipulate the functions
    result_button = Button(buttons_frame, text="Display Result", font=("verdana", "10"), width=16, bg="#64F0AB",
                           fg="#0C4529", activebackground="#3AC982", activeforeground="#FFFFFF", relief=GROOVE,
                           command=display_result)
    generate_button = Button(buttons_frame, text="Generate Marksheet", font=("verdana", "10"), width=20, bg="#6EF5FA",
                             fg="#144E50", activebackground="#1DCAD1", activeforeground="#FFFFFF", relief=GROOVE,
                             state="disabled", command=generate_marksheet)
    reset_button = Button(buttons_frame, text="Reset Entries", font=("verdana", "10"), width=15, bg="#E3FF00",
                          fg="#454B14", activebackground="#A7B817", activeforeground="#FFFFFF", relief=GROOVE,
                          command=reset)
    exit_button = Button(buttons_frame, text="Exit", font=("verdana", "10"), width=6, bg="#FF0007", fg="#FFFFFF",
                         activebackground="#AE1318", activeforeground="#FFFFFF", relief=GROOVE, command=exit)

    # using the grid() method to set the positions of these buttons in a grid format
    result_button.grid(row=0, column=0, padx=2.5, pady=10)
    generate_button.grid(row=0, column=1, padx=2.5, pady=10)
    reset_button.grid(row=0, column=2, padx=2.5, pady=10)
    exit_button.grid(row=0, column=3, padx=2.5, pady=10)


    loginButton = Button(gui_root, text='Menu', font=('Open Sans', '9', 'bold underline'), bg='white', fg='#af12c4', bd=0,
                         cursor='hand2', activebackground='white', activeforeground='purple',
                         command=marksheet_page)
    loginButton.place(x=18, y=5)



    # using the mainloop() method to run the application
    gui_root.mainloop()
