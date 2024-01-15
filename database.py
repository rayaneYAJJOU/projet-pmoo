# database.py
import sqlite3

def setup_database():
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()

    # Create tables for Users, Teachers, Students, Courses, Grades, Absences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'teacher', 'student'))
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL,
            class TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Grades (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES Students(id),
            FOREIGN KEY (course_id) REFERENCES Courses(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Absences (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            student_id INTEGER,
            date TEXT NOT NULL,
            present INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(id)
        )
    ''')
    conn.commit()
    conn.close()
    insert_initial_users()

def insert_initial_users():
    users = [
        (0, "admin", "password", "admin"),
        (1, "a","a","admin")
    ]
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    for id, username, password, role in users:
        cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO Users (id, username, password, role) VALUES (?, ?, ?, ?)", (id, username, password, role))
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

def insert_teacher(name, subject,username, password):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Teachers (name, subject) VALUES (?, ?)", (name, subject))
    cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, 'student')", (username, password))
    conn.commit()
    conn.close()

def insert_student(name, class_,username, password):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, class) VALUES (?, ?)", (name, class_))
    cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, 'student')", (username, password))
    conn.commit()
    conn.close()

# Additional functions for managing courses, grades, and absences can be added here as needed.
