# student.py
import tkinter as tk
import sqlite3

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


def show_student_interface(student_id):
    student_window = tk.Tk()
    student_window.title("Student Dashboard")

    courses, grades, absences = get_student_data(student_id)

    # Display sections
    display_section(student_window, "Courses:", courses, 0)
    display_section(student_window, "Grades:", [(f"{grade[0]}: {grade[1]}",) for grade in grades], len(courses) + 1)
    display_absence(student_window, "Absences:", absences, len(courses) + len(grades) + 2)

    student_window.mainloop()

# This file is saved as 'student.py' and is part of the overall application.
