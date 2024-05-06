import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import sqlite3

window=tk.Tk()
window.title("Data Entry form") 

frame=tk.Frame(window)
frame.pack()

def submit():

    accepted=accept_var.get()

    if accepted=="Accepted":

        Firstname = firstname_entry.get()
        Lastname = lastname_entry.get()

        if Firstname and Lastname:
            User_ID=ID_entry.get()
            if User_ID:
                Title = title_combobox.get()
                Age = age_spinbox.get()
                Nationality = nationality_entry.get()
                
                Registration = reg_status_var.get()
                Courses = numcourses_spinbox.get()
                Semesters = numsemesters_spinbox.get()
                
                conn = sqlite3.connect('Client_data.db')
                cursor=conn.cursor()
                table_create_query = '''CREATE TABLE IF NOT EXISTS Client_Data 
                        (User_ID TEXT PRIMARY KEY, Firstname TEXT, Lastname TEXT, Title TEXT, Age INT, Nationality TEXT, 
                        Registration TEXT, Courses INT, Semesters INT)'''
                conn.execute(table_create_query)

                cursor.execute('''SELECT * FROM Client_Data WHERE User_ID=?''', (User_ID,))
                existing_record = cursor.fetchone()

                if existing_record:
                    tk.messagebox.showwarning(title="Error", message="A record with this User ID already exists.")

                else:
                    data_insert_query = '''INSERT INTO Client_Data (User_ID, Firstname, Lastname, Title, Age, Nationality, Registration, Courses, Semesters) 
                            VALUES (?,?,?,?,?,?,?,?,?)'''
                    data_insert_tuple=(User_ID,Firstname,Lastname,Title,Age,Nationality,Registration,Courses,Semesters)
                    cursor=conn.cursor()
                    cursor.execute(data_insert_query, data_insert_tuple)
                    conn.commit()
                    conn.close()
                    tk.messagebox.showinfo(title="Success", message="Record Added Successfully.")
            else:
                tk.messagebox.showwarning(title="Error", message="A User ID is required.")
        else:
            tk.messagebox.showwarning(title="Error", message="First Name and Last Name are required.")
    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted our Terms and Condtitions.")

    clear_fields()

def update(): 
    def fetch_record():
        search_id = UD_entry.get()

        conn = sqlite3.connect('Client_data.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM Client_Data WHERE User_ID=?''', (search_id,))
        search_result = cursor.fetchone()

        conn.close()

        if search_result:
            updated_fn_entry.delete(0, tk.END)
            updated_fn_entry.insert(0, search_result[1])
            updated_ln_entry.delete(0, tk.END)
            updated_ln_entry.insert(0, search_result[2])
            updated_t_entry.delete(0, tk.END)
            updated_t_entry.insert(0, search_result[3])
            updated_a_entry.delete(0, tk.END)
            updated_a_entry.insert(0, search_result[4])
            updated_n_entry.delete(0, tk.END)
            updated_n_entry.insert(0, search_result[5])
            updated_reg_entry.delete(0, tk.END)
            updated_reg_entry.insert(0, search_result[6])
            updated_cour_entry.delete(0, tk.END)
            updated_cour_entry.insert(0, search_result[7])
            updated_sems_entry.delete(0, tk.END)
            updated_sems_entry.insert(0, search_result[8])
        else:
            tk.messagebox.showwarning(title="Error", message="No record found!")   

    def updaterecord():
        User_ID = UD_entry.get()
        Fname = updated_fn_entry.get()
        Lname = updated_ln_entry.get()
        Tit = updated_t_entry.get()
        A = updated_a_entry.get()
        Nation = updated_n_entry.get()
        Reg = updated_reg_entry.get()
        Course = updated_cour_entry.get()
        Semester = updated_sems_entry.get()
            
        conn= sqlite3.connect("Client_data.db")
        cursor= conn.cursor()
            
        cursor.execute('''UPDATE Client_Data SET Firstname=?, Lastname=?, Title=?, Age=?, Nationality=?, Registration=?, Courses=?, Semesters=?
                       WHERE User_ID=?''',(Fname, Lname, Tit, A, Nation, Reg, Course, Semester, User_ID))
        conn.commit()
        conn.close()
        addroot.destroy()
        tk.messagebox.showinfo(title="Success", message="Record Updated Successfully.")

    addroot = Toplevel(master=window)
    addroot.grab_set()
    addroot.geometry("380x480")
    addroot.title("Update record")

    UD_label= tk.Label(addroot, text="Enter User ID:", padx=20, pady=10)
    UD_label.grid(row=0, column=2)
    UD_entry= Entry(addroot)
    UD_entry.grid(row=1, column=2)

    btn_fetch = Button(addroot, text="Fetch Record", command=fetch_record)
    btn_fetch.grid(row=3,column=2, padx=20, pady= 10)

    updated_fn_label=tk.Label(addroot, text="Updated First Name:")
    updated_fn_label.grid(row=5,column=2, padx=20, pady=10)
    updated_fn_entry = Entry(addroot)
    updated_fn_entry.grid(row=5, column=3,padx=20, pady=10)
            
    updated_ln_label=tk.Label(addroot, text="Updated Last Name:")
    updated_ln_label.grid(row=6,column=2,padx=20, pady=10)
    updated_ln_entry =Entry(addroot)
    updated_ln_entry.grid(row=6,column=3,padx=20, pady=10)
            
    updated_t_label=tk.Label(addroot, text="Updated Title:")
    updated_t_label.grid(row=7,column=2,padx=20, pady=10)
    updated_t_entry = Entry(addroot)
    updated_t_entry.grid(row=7,column=3,padx=20, pady=10)
            
    updated_a_label=tk.Label(addroot, text="Updated Age:")
    updated_a_label.grid(row=8,column=2,padx=20, pady=10)
    updated_a_entry = Entry(addroot)
    updated_a_entry.grid(row=8,column=3,padx=20, pady=10)

    updated_n_label=tk.Label(addroot, text="Updated Nationality:")
    updated_n_label.grid(row=9,column=2,padx=20, pady=10)
    updated_n_entry = Entry(addroot)
    updated_n_entry.grid(row=9,column=3,padx=20, pady=10)
            
    updated_reg_label=tk.Label(addroot, text="Updated Registration:")
    updated_reg_label.grid(row=10,column=2,padx=20, pady=10)
    updated_reg_entry = Entry(addroot)
    updated_reg_entry.grid(row=10,column=3,padx=20, pady=10)
            
    updated_cour_label=tk.Label(addroot, text="Updated Courses:")
    updated_cour_label.grid(row=11,column=2,padx=20, pady=10)
    updated_cour_entry = Entry(addroot)
    updated_cour_entry.grid(row=11,column=3,padx=20, pady=10)
            
    updated_sems_label=tk.Label(addroot, text="Updated Semesters:")
    updated_sems_label.grid(row=12,column=2,padx=20, pady=10)
    updated_sems_entry = tk.Entry(addroot)
    updated_sems_entry.grid(row=12,column=3,padx=20, pady=10)
        
    btn = tk.Button(addroot, text="Update", command=updaterecord)
    btn.grid(row=13,column=2,padx=21, pady=10)



def search():
    def searchrecord():
        search_id = UserID.get()

        conn = sqlite3.connect('Client_data.db')
        cursor = conn.cursor()

        if search_id:
            cursor.execute('''SELECT * FROM Client_Data WHERE User_ID=?''', (search_id,))
            search_results = cursor.fetchall()
            if search_results:
                display_search_results(search_results)
            else:
                tk.messagebox.showwarning(title="Error", message="No User found")

        conn.close()
        addroot.destroy()

    addroot = Toplevel(master=window)
    addroot.grab_set()
    addroot.title("Search record")

    title_frame=tk.LabelFrame(addroot, text="Search by User ID", padx=20, pady=10)
    title_frame.grid(row=0, column=0)
    entry_label=tk.Label(title_frame, text="Enter User ID:", padx=20, pady=10)
    entry_label.grid(row=0,column=0)
    UserID = tk.Entry(title_frame)
    UserID.grid(row=2,column=0)

    btn = tk.Button(title_frame, text="Search", command=searchrecord)
    btn.grid(row=4, column=0,padx=20, pady=10)


def delete():
    def deleterecord():
        U_id = UserID.get()

        conn = sqlite3.connect('Client_data.db')
        cursor = conn.cursor()
        
        cursor.execute('''DELETE FROM Client_Data WHERE User_ID=?''', (U_id,))
        conn.commit()
        conn.close()
        
        tk.messagebox.showinfo(title="Success", message="Record Deleted Successfully.")
        
        addroot.destroy()
        
    addroot = Toplevel(master=window)
    addroot.grab_set()
    addroot.geometry("470x200")
    addroot.title("Delete record")
    addroot.config()

    tk.Label(addroot, text="Enter User ID:", padx=20, pady=10).pack()
    UserID = tk.Entry(addroot)
    UserID.pack(padx=20, pady=10)

    btn = tk.Button(addroot, text="Delete", command=deleterecord)
    btn.pack(padx=20, pady=10)
    
def clear_fields():
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    title_combobox.delete(0, END)
    age_spinbox.delete(0, END)
    nationality_entry.delete(0, END)
    ID_entry.delete(0, END)
    reg_status_var.set("Not Registered")
    numcourses_spinbox.delete(0, END)
    numsemesters_spinbox.delete(0, END)
    accept_var.set("Not Accepted")

def display_search_results(results):
        results_window=Toplevel(master=window)
        results_window.geometry("600x400")
        treeview = ttk.Treeview(results_window)
        treeview.pack()

        treeview["columns"] = ("ID", "First Name", "Last Name", "Title", "Age", "Nationality", "Resgistration Status", "No. Courses", "No. Semesters")

        # Format columns
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("ID", anchor=E, width=70)
        treeview.column("First Name", anchor=E, width=70)
        treeview.column("Last Name", anchor=E, width=100)
        treeview.column("Title", anchor=E, width=70)
        treeview.column("Age", anchor=E, width=70)
        treeview.column("Nationality", anchor=E, width=70)
        treeview.column("Resgistration Status", anchor=E, width=70)
        treeview.column("No. Courses", anchor=E, width=70)
        treeview.column("No. Semesters", anchor=E, width=70)

        treeview.heading("#0", text="", anchor=W)
        treeview.heading("ID", text="ID", anchor=W)
        treeview.heading("First Name", text="First Name", anchor=W)
        treeview.heading("Last Name", text="Last Name", anchor=W)
        treeview.heading("Title", text="Title", anchor=W)
        treeview.heading("Age", text="Age", anchor=W)
        treeview.heading("Nationality", text="Nationality", anchor=W)
        treeview.heading("Resgistration Status", text="Resgistration Status", anchor=W)
        treeview.heading("No. Courses", text="No. Courses", anchor=W)
        treeview.heading("No. Semesters", text="No. Semesters", anchor=W)

        for row in results:
            treeview.insert("", END, values=row)

def display():
    conn= sqlite3.connect('Client_data.db')
    cursor= conn.cursor()

    results_window=Toplevel(master=window)
    treeview = ttk.Treeview(results_window)
    treeview.pack()

    treeview["columns"] = ("ID", "First Name", "Last Name", "Title", "Age", "Nationality", "Resgistration Status", "No. Courses", "No. Semesters")

    cursor.execute("SELECT * from Client_Data")
    data= cursor.fetchall()

    treeview.column("#0", width=0, stretch=NO)
    treeview.column("ID", anchor=E, width=70)
    treeview.column("First Name", anchor=E, width=70)
    treeview.column("Last Name", anchor=E, width=100)
    treeview.column("Title", anchor=E, width=70)
    treeview.column("Age", anchor=E, width=70)
    treeview.column("Nationality", anchor=E, width=70)
    treeview.column("Resgistration Status", anchor=E, width=70)
    treeview.column("No. Courses", anchor=E, width=70)
    treeview.column("No. Semesters", anchor=E, width=70)

    treeview.heading("#0", text="", anchor=W)
    treeview.heading("ID", text="ID", anchor=W)
    treeview.heading("First Name", text="First Name", anchor=W)
    treeview.heading("Last Name", text="Last Name", anchor=W)
    treeview.heading("Title", text="Title", anchor=W)
    treeview.heading("Age", text="Age", anchor=W)
    treeview.heading("Nationality", text="Nationality", anchor=W)
    treeview.heading("Resgistration Status", text="Resgistration Status", anchor=W)
    treeview.heading("No. Courses", text="No. Courses", anchor=W)
    treeview.heading("No. Semesters", text="No. Semesters", anchor=W)

    for row in data:
        treeview.insert("", END, values=row)


action_frame=tk.LabelFrame(frame, text="Actions")
action_frame.grid(row=0, column=0)
btn_update = Button(action_frame, text="Update", bg="#ADD8E6", command=update)
btn_update.grid(row=0, column=0,padx=20, pady=10)
btn_search = Button(action_frame, text="Search", bg="#ADD8E6", command=search)
btn_search.grid(row=0, column=1,padx=20, pady=10)
btn_delete = Button(action_frame, text="Delete", bg="#ADD8E6", command=delete)
btn_delete.grid(row=0, column=2,padx=20, pady=10)
btn_display = Button(action_frame, text="Display", bg="#ADD8E6", command=display)
btn_display.grid(row=0, column=3,padx=20, pady=10)

user_info_frame=tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=1, column=0, padx=20, pady=10)

firstname_label=tk.Label(user_info_frame, text="First Name")
firstname_label.grid(row=0, column=0)
lastname_label=tk.Label(user_info_frame, text="Last Name")
lastname_label.grid(row=0, column=1)

firstname_entry=tk.Entry(user_info_frame)
firstname_entry.grid(row=1, column=0)
lastname_entry=tk.Entry(user_info_frame)
lastname_entry.grid(row=1, column=1)

title_label=tk.Label(user_info_frame, text="Title")
title_combobox=ttk.Combobox(user_info_frame, values=["Ms.", "Mr.", "Mrs.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label=tk.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox=tk.Spinbox(user_info_frame, from_=18, to=80)
age_spinbox.grid(row=3, column=0)

nationality_label=tk.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_entry=tk.Entry(user_info_frame)
nationality_entry.grid(row=3, column=1)

ID_label=tk.Label(user_info_frame, text="User ID")
ID_label.grid(row=2, column=2)
ID_entry=tk.Entry(user_info_frame)
ID_entry.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

course_frame=tk.LabelFrame(frame)
course_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

registed_label=tk.Label(course_frame, text="Registration status")
registed_label.grid(row=0, column=0)
reg_status_var=tk.StringVar(value="Not Registered")
registered_check=tk.Checkbutton(course_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered" , offvalue="Not Registered")
registered_check.grid(row=1, column=0)

numcourses_label=tk.Label(course_frame, text="#Completed Courses")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox=tk.Spinbox(course_frame, from_=0, to='infinity')
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label=tk.Label(course_frame, text="#Semesters")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox=tk.Spinbox(course_frame, from_=0, to='infinity')
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame=tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

accept_var=tk.StringVar(value="Not Accepted")

terms_check=tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

button=tk.Button(frame, text="Submit", command=submit)
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

display_label = Label(window, text="")
display_label.pack()

window.mainloop()    