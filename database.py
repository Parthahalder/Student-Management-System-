import sqlite3

def connect_db():
    return sqlite3.connect("student_mgmt.db")

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Tables for students, attendance, grades, communication
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER,
            name TEXT NOT NULL,
            class TEXT NOT NULL,
            roll_no INTEGER UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            student_id INTEGER,
            date TEXT,
            status TEXT CHECK(status IN ('Present', 'Absent'))
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            student_id INTEGER,
            subject TEXT,
            grade TEXT
            
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            student_id INTEGER,
            message TEXT,
            by TEXT CHECK(by IN ('Teacher', 'Parent', 'Student'))
            )
    ''')

    conn.commit()
    conn.close()
