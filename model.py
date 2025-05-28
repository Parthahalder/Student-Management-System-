from database import connect_db

def enroll_student(student_id, name, class_name, roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (student_id, name, class, roll_no) VALUES (?, ?, ?, ?)", (student_id, name, class_name, roll_no))
    conn.commit()
    conn.close()

def mark_attendance(student_id, date, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)", (student_id, date, status))
    conn.commit()
    conn.close()

def record_grade(student_id, subject, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
    conn.commit()
    conn.close()

def send_message(student_id, message, sender):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (student_id, message, by) VALUES (?, ?, ?)", (student_id, message, sender))
    conn.commit()
    conn.close()

def get_student_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    student = cursor.fetchone()
    conn.close()
    return student

def get_attendance(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT date, status FROM attendance WHERE student_id = ?", (student_id,))
    records = cursor.fetchall()
    conn.close()
    return records

def get_grades(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT subject, grade FROM grades WHERE student_id = ?", (student_id,))
    grades = cursor.fetchall()
    conn.close()
    return grades

def get_messages(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT message, by FROM messages WHERE student_id = ?", (student_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages

