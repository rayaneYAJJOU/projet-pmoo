# database.py
import sqlite3

def setup_database():
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()

    # Create tables for Users, Teachers, Students, Courses, Grades, Absences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'teacher', 'student'))
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            class TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Grades (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES Students(id),
            FOREIGN KEY (course_id) REFERENCES Courses(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Absences (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Students(id)
        )
    ''')
    conn.commit()
    conn.close()
    insert_initial_users()

def insert_initial_users():
    users = [
        ("admin", "admin123", "admin"),
        ("teacher", "teacher123", "teacher"),
        ("student", "student123", "student")
    ]
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    for username, password, role in users:
        cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM Users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def insert_user(username, password, role):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()

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

# Additional functions for managing courses, grades, and absences can be added here as needed.

if __name__ == "__main__":
    setup_database()
    # Example: setup default admin account
    insert_user("admin", "admin123", "admin")
