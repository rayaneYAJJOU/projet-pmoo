# admin.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def insert_teacher(name, subject):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Teachers (name, subject) VALUES (?, ?)", (name, subject))
    conn.commit()
    conn.close()

def insert_student(name, class_):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, class) VALUES (?, ?)", (name, class_))
    conn.commit()
    conn.close()

def show_admin_interface():
    admin_window = tk.Tk()
    admin_window.title("Admin Dashboard")

    # Teacher input fields
    tk.Label(admin_window, text="Teacher's Name:").grid(row=0, column=0)
    teacher_name_entry = tk.Entry(admin_window)
    teacher_name_entry.grid(row=0, column=1)

    tk.Label(admin_window, text="Subject:").grid(row=1, column=0)
    teacher_subject_entry = tk.Entry(admin_window)
    teacher_subject_entry.grid(row=1, column=1)

    def add_teacher():
        name = teacher_name_entry.get()
        subject = teacher_subject_entry.get()
        if name and subject:
            insert_teacher(name, subject)
            messagebox.showinfo("Success", "Teacher added successfully")
        else:
            messagebox.showwarning("Warning", "All fields are required")

    tk.Button(admin_window, text="Add Teacher", command=add_teacher).grid(row=2, columnspan=2)

    # Student input fields
    tk.Label(admin_window, text="Student's Name:").grid(row=3, column=0)
    student_name_entry = tk.Entry(admin_window)
    student_name_entry.grid(row=3, column=1)

    tk.Label(admin_window, text="Class:").grid(row=4, column=0)
    student_class_entry = tk.Entry(admin_window)
    student_class_entry.grid(row=4, column=1)

    def add_student():
        name = student_name_entry.get()
        class_ = student_class_entry.get()
        if name and class_:
            insert_student(name, class_)
            messagebox.showinfo("Success", "Student added successfully")
        else:
            messagebox.showwarning("Warning", "All fields are required")

    tk.Button(admin_window, text="Add Student", command=add_student).grid(row=5, columnspan=2)

    admin_window.mainloop()

# This file would be saved as 'admin.py' and used as part of the overall application.
