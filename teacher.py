# teacher.py
import shutil
import tkinter as tk
import os
from tkinter import messagebox, filedialog
import sqlite3

def show_pdf_files():
    pdf_directory = 'cours'

    all_files = os.listdir(pdf_directory)
    pdf_files = [f for f in all_files if f.endswith('.pdf')]

    if pdf_files:
        messagebox.showinfo("PDF Files", "\n".join(pdf_files))
    else:
        messagebox.showinfo("PDF Files", "No PDF files found in the directory.")

def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        target_directory = 'cours'

        file_name = file_path.split('/')[-1]

        target_path = os.path.join(target_directory, file_name)

        try:
            shutil.copy(file_path, target_path)
            messagebox.showinfo("Success", "PDF uploaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showinfo("Cancelled", "No file selected")

def modify_pdf():
    file_path_to_replace = filedialog.askopenfilename(title="Select PDF to Modify", filetypes=[("PDF files", "*.pdf")])

    if file_path_to_replace:
        new_file_path = filedialog.askopenfilename(title="Select New PDF", filetypes=[("PDF files", "*.pdf")])

        if new_file_path:
            try:
                shutil.copy(new_file_path, file_path_to_replace)
                messagebox.showinfo("Success", "PDF modified successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showinfo("Cancelled", "No new file selected")
    else:
        messagebox.showinfo("Cancelled", "No file selected to modify")

def delete_pdf():
    file_path = filedialog.askopenfilename(title="Select PDF to Delete", filetypes=[("PDF files", "*.pdf")])

    if file_path:
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{os.path.basename(file_path)}'?"):
            try:
                os.remove(file_path)
                messagebox.showinfo("Success", "PDF deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showinfo("Cancelled", "Deletion cancelled")
    else:
        messagebox.showinfo("Cancelled", "No file selected")

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

    # Add buttons for PDF functionalities
    tk.Button(teacher_window, text="Show PDF Files", command=show_pdf_files).grid(row=5, columnspan=2)
    tk.Button(teacher_window, text="Upload PDF", command=upload_pdf).grid(row=6, columnspan=2)
    tk.Button(teacher_window, text="Modify PDF", command=modify_pdf).grid(row=7, columnspan=2)
    tk.Button(teacher_window, text="Delete PDF", command=delete_pdf).grid(row=8, columnspan=2)

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