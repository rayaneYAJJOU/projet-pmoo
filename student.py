# student.py
import os
import subprocess
import tkinter as tk
import sqlite3
from tkinter import messagebox

def get_student_data(student_id):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()

    # Fetch courses
    cursor.execute("SELECT c.name FROM Courses c JOIN Grades g ON c.id = g.course_id WHERE g.student_id = ?", (student_id,))
    courses = cursor.fetchall()

    # Fetch grades
    cursor.execute("SELECT c.name, g.grade FROM Courses c JOIN Grades g ON c.id = g.course_id WHERE g.student_id = ?", (student_id,))
    grades = cursor.fetchall()

    # Fetch absences
    cursor.execute("SELECT date, present FROM Absences WHERE student_id = ?", (student_id,))
    absences = cursor.fetchall()
    print(courses, grades, absences, "id",student_id)
    conn.close()
    return courses, grades, absences

def display_section(window, title, data, start_row):
    tk.Label(window, text=title).grid(row=start_row, column=0)
    for idx, item in enumerate(data):
        tk.Label(window, text=f"{idx + 1}/{item[0]}").grid(row=start_row + idx + 1, column=0)

def display_absence(window, title, data, start_row):
    tk.Label(window, text=title).grid(row=start_row, column=0)
    for idx, item in enumerate(data):
        tk.Label(window, text=f"{idx + 1}/date {item[0]}- present :{bool(item[1])}").grid(row=start_row + idx + 1, column=0)

def list_pdf_files(student_window, start_row):
    # Directory where the PDF files are stored
    pdf_directory = 'cours'  # Adjust this to the directory containing the PDFs

    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

    # Create a Listbox widget to display the PDF files
    lb = tk.Listbox(student_window)
    for file in pdf_files:
        lb.insert(tk.END, file)
    lb.grid(row=start_row, column=0, columnspan=2)

    # Button to open the selected PDF file
    def open_pdf():
        selected_file = lb.get(lb.curselection())
        if selected_file:
            # Full path to the file
            file_path = os.path.join(pdf_directory, selected_file)

            try:
                # Cross-platform way to open a file with the default application
                if os.name == 'nt':  # Windows
                    os.startfile(file_path)
                elif os.name == 'posix':  # macOS, Linux
                    subprocess.Popen(['open', file_path] if sys.platform == 'darwin' else ['xdg-open', file_path])
                else:
                    messagebox.showerror("Error", "Unsupported operating system")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    tk.Button(student_window, text="Open PDF", command=open_pdf).grid(row=start_row + 1, column=0, columnspan=2)

def show_student_interface(student_id):
    student_window = tk.Tk()
    student_window.title("Student Dashboard")

    courses, grades, absences = get_student_data(student_id)

    # Existing display code...

    # Function call to list and open PDF files
    list_pdf_files(student_window, len(courses) + len(grades) + len(absences) + 3)

    student_window.mainloop()

def show_student_interface(student_id):
    student_window = tk.Tk()
    student_window.title("Student Dashboard")

    courses, grades, absences = get_student_data(student_id)

    # Display sections
    display_section(student_window, "Courses:", courses, 0)
    display_section(student_window, "Grades:", [(f"{grade[0]}: {grade[1]}",) for grade in grades], len(courses) + 1)
    display_absence(student_window, "Absences:", absences, len(courses) + len(grades) + 2)

    student_window = tk.Tk()
    student_window.title("Student Dashboard")

    courses, grades, absences = get_student_data(student_id)

    # Function call to list and open PDF files
    list_pdf_files(student_window, len(courses) + len(grades) + len(absences) + 3)

    student_window.mainloop()


# This file is saved as 'student.py' and is part of the overall application.
