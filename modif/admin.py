# admin.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def insert_teacher(name, subject, username, password, id):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    #adding the teacher to the Teacher database
    cursor.execute("INSERT INTO Teachers (name, subject, id) VALUES (?, ?, ?)", (name, subject, id))
    cursor.execute("INSERT INTO Courses (name, id, teacher_id) VALUES (?, ?, ?)", (subject, id, id))
    cursor.execute("INSERT INTO Users (id, username, password, role) VALUES (?, ?, ?, 'teacher')", (id ,username, password))
    cursor.execute("SELECT id FROM Students")
    info = cursor.fetchall()
    for s_id in info:
        print(s_id)
        cursor.execute("INSERT INTO Grades (grade, course_id, student_id, id) VALUES (?, ?, ?, ?)", (-1, id, s_id, id))
    conn.commit()
    conn.close()

def insert_student(name, class_, username, password, s_id):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, class, id) VALUES (?, ?, ?)", (name, class_, s_id))
    cursor.execute("INSERT INTO Users (id, username, password, role) VALUES (?, ?, ?, 'student')", (s_id, username, password))
    cursor.execute("SELECT id, name FROM Courses c")
    info = cursor.fetchall()
    for c_id, _ in info:
        cursor.execute("INSERT INTO Grades (grade, course_id, student_id, id) VALUES (?, ?, ?, ?)", (-1, c_id, s_id, c_id))
    conn.commit()
    conn.close()

def show_admin_interface():
    admin_window = tk.Tk()
    admin_window.title("Admin Dashboard")

    # Teacher input fields
    tk.Label(admin_window, text="Teacher's Name:").grid(row=0, column=0)
    teacher_name_entry = tk.Entry(admin_window)
    teacher_name_entry.grid(row=0, column=1)

    tk.Label(admin_window, text="Teacher's username:").grid(row=0, column=2)
    teacher_username_entry = tk.Entry(admin_window)
    teacher_username_entry.grid(row=0, column=3)

    tk.Label(admin_window, text="Teacher's id:").grid(row=0, column=4)
    teacher_id_entry = tk.Entry(admin_window)
    teacher_id_entry.grid(row=0, column=5)

    tk.Label(admin_window, text="Teacher's password:").grid(row=1, column=2)
    teacher_password_entry = tk.Entry(admin_window)
    teacher_password_entry.grid(row=1, column=3)

    tk.Label(admin_window, text="Subject:").grid(row=1, column=0)
    teacher_subject_entry = tk.Entry(admin_window)
    teacher_subject_entry.grid(row=1, column=1)

    def add_teacher():
        name = teacher_name_entry.get()
        subject = teacher_subject_entry.get()
        user = teacher_username_entry.get()
        mdp = teacher_password_entry.get()
        id = teacher_id_entry.get()
        if name and subject and user and mdp:
            insert_teacher(name, subject, user, mdp, id)
            messagebox.showinfo("Success", "Teacher added successfully")
        else:
            messagebox.showwarning("Warning", "All fields are required")

    tk.Button(admin_window, text="Add Teacher", command=add_teacher).grid(row=2, columnspan=2)

    # Student input fields
    tk.Label(admin_window, text="Student's Name:").grid(row=3, column=0)
    student_name_entry = tk.Entry(admin_window)
    student_name_entry.grid(row=3, column=1)

    tk.Label(admin_window, text="Student's username:").grid(row=3, column=2)
    student_username_entry = tk.Entry(admin_window)
    student_username_entry.grid(row=3, column=3)

    tk.Label(admin_window, text="Student's id:").grid(row=3, column=4)
    student_id_entry = tk.Entry(admin_window)
    student_id_entry.grid(row=3, column=5)

    tk.Label(admin_window, text="Student's password:").grid(row=4, column=2)
    student_password_entry = tk.Entry(admin_window)
    student_password_entry.grid(row=4, column=3)

    tk.Label(admin_window, text="Class:").grid(row=4, column=0)
    student_class_entry = tk.Entry(admin_window)
    student_class_entry.grid(row=4, column=1)

    def add_student():
        name = student_name_entry.get()
        class_ = student_class_entry.get()
        user = student_username_entry.get()
        mdp = student_password_entry.get()
        id = student_id_entry.get()
        print("id", id)

        if name and class_:
            insert_student(name, class_,user,mdp,id)
            messagebox.showinfo("Success", "Student added successfully")
        else:
            messagebox.showwarning("Warning", "All fields are required")

    tk.Button(admin_window, text="Add Student", command=add_student).grid(row=5, columnspan=2)

    admin_window.mainloop()

# This file would be saved as 'admin.py' and used as part of the overall application.
