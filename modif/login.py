# login.py
import tkinter as tk
from tkinter import messagebox
from database import login
from admin import show_admin_interface
from teacher import show_teacher_interface
from student import show_student_interface
import sqlite3

def create_login_screen():
    window = tk.Tk()
    window.title("School Management System Login")

    # Username and password labels and entries
    tk.Label(window, text="Username").grid(row=0, column=0)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    tk.Label(window, text="Password").grid(row=1, column=0)
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    # Function to handle login attempt
    def attempt_login():
        conn = sqlite3.connect('school_management.db')
        cursor = conn.cursor()
        username = username_entry.get()
        password = password_entry.get()
        user_role = login(username, password)
        if user_role:
            window.destroy()
            if user_role[0] == 'admin':
                show_admin_interface()
            elif user_role[0] == 'teacher':
                cursor.execute("SELECT id FROM Users WHERE username = ? AND password = ?",(username, password))
                teacher_id=cursor.fetchall()[0][0]
                show_teacher_interface(teacher_id)
            elif user_role[0] == 'student':
                cursor.execute("SELECT id FROM Users WHERE username = ? AND password = ?",(username, password))
                student_id=cursor.fetchall()[0][0]
                print("lid",student_id)
                show_student_interface(student_id)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
        conn.commit()
        conn.close()

    # Login button
    login_button = tk.Button(window, text="Login", command=attempt_login)
    login_button.grid(row=2, column=1)

    window.mainloop()

if __name__ == "__main__":
    create_login_screen()