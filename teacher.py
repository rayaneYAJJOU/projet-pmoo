# teacher.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def get_students():
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students

def update_grade(student_id, course_id, grade):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    print(student_id, course_id, grade)
    cursor.execute("UPDATE Grades SET grade = ? WHERE student_id = ? AND course_id = ?", (grade, student_id, course_id))
    conn.commit()
    conn.close()

def show_teacher_interface(t_id):
    teacher_window = tk.Tk()
    teacher_window.title("Teacher Dashboard")

    # Select student dropdown
    tk.Label(teacher_window, text="Select Student:").grid(row=0, column=0)
    students = get_students()
    selected_student = tk.StringVar(teacher_window)
    selected_student.set(students[0][1])  # default value
    student_menu = tk.OptionMenu(teacher_window, selected_student, *[student[1] for student in students])
    student_menu.grid(row=0, column=1)

    # Grade input
    tk.Label(teacher_window, text="Grade:").grid(row=1, column=0)
    grade_entry = tk.Entry(teacher_window)
    grade_entry.grid(row=1, column=1)

    # Add courses


    def submit_grade():
        student_name = selected_student.get()
        student_id = [student[0] for student in students if student[1] == student_name][0]
        grade = grade_entry.get()
        # Assume course_id is predetermined or selected from another dropdown
        course_id = t_id
        
        update_grade(student_id, course_id, grade)
        messagebox.showinfo("Success", "Grade updated successfully")

    tk.Button(teacher_window, text="Submit Grade", command=submit_grade).grid(row=2, columnspan=2)

    # Absence input
    tk.Label(teacher_window, text="Absence:").grid(row=3, column=0)
    absence_entry = tk.Entry(teacher_window)
    absence_entry.grid(row=3, column=1)

    tk.Label(teacher_window, text="Absence date:").grid(row=3, column=2)
    absence_date_entry = tk.Entry(teacher_window)
    absence_date_entry.grid(row=3, column=3)

    def submit_absence():
        student_name = selected_student.get()
        student_id = [student[0] for student in students if student[1] == student_name][0]
        absence = absence_entry.get()
        absence_date = absence_date_entry.get()
        
        add_absence(student_id, absence_date,absence)
        messagebox.showinfo("Success", "Grade updated successfully")

    tk.Button(teacher_window, text="Submit Absence", command=submit_absence).grid(row=4, columnspan=2)



    teacher_window.mainloop()

'''def get_current_grade(student_id, course_id):
   conn = sqlite3.connect('school_management.db')
   cursor = conn.cursor()
   cursor.execute("SELECT grade FROM Grades WHERE student_id = ? AND course_id = ?", (student_id, course_id))
   grade = cursor.fetchone()
   conn.close()
   return grade[0] if grade else "N/A"'''
    
'''def get_absences(student_id):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date FROM Absences WHERE student_id = ?", (student_id,))
    absences = cursor.fetchall()
    conn.close()
    return [absence[0] for absence in absences]'''

def add_absence(student_id, date, present):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Absences (student_id, date,present) VALUES (?, ?, ?)", (student_id, date, present))
    conn.commit()
    conn.close()