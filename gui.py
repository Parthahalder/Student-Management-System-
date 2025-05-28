import tkinter as tk
from tkinter import messagebox
from model import (
     enroll_student, mark_attendance, record_grade, send_message,
    get_student_by_name, get_attendance, get_grades, get_messages
)



root = tk.Tk()
root.title("Student Management System")
root.geometry("750x650")

# ===== Functions =====

def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, tk.END)

def add_student():
    student_id = id_entry.get()
    name = name_entry.get()
    class_ = class_entry.get()
    roll = roll_entry.get()
    if student_id and name and class_ and roll:
        enroll_student(student_id, name, class_, int(roll))
        messagebox.showinfo("Success", f"Student '{name}' added.")
        clear_entries(id_entry,name_entry, class_entry, roll_entry)
    else:
        messagebox.showwarning("Input Error", "Fill all student fields.")

def mark_attendance_gui():
    name = att_name_entry.get()
    date = att_date_entry.get()
    status = status_entry.get()

    student = get_student_by_name(name)
    if student:
        mark_attendance(student[0], date, status)
        messagebox.showinfo("Success", f"Attendance marked for {name}.")
        clear_entries(att_name_entry, att_date_entry, status_entry)
    else:
        messagebox.showerror("Not Found", f"Student '{name}' not found.")

def record_grades_gui():
    name = grade_name_entry.get()
    subject = subject_entry.get()
    grade = grade_entry.get()

    student = get_student_by_name(name)
    if student:
        record_grade(student[0], subject, grade)
        messagebox.showinfo("Success", f"Grade recorded for {name}.")
        clear_entries(grade_name_entry, subject_entry, grade_entry)
    else:
        messagebox.showerror("Not Found", f"Student '{name}' not found.")

def send_msg_gui():
    name = msg_name_entry.get()
    sender = sender_entry.get()
    msg = msg_entry.get()

    student = get_student_by_name(name)
    if student:
        send_message(student[0], msg, sender)
        messagebox.showinfo("Sent", "Message sent.")
        clear_entries(msg_name_entry, sender_entry, msg_entry)
    else:
        messagebox.showerror("Not Found", f"Student '{name}' not found.")

def search_student():
    name = search_name_entry.get().strip()
    result_text.delete("1.0", tk.END)

    student = get_student_by_name(name)
    if not student:
        result_text.insert(tk.END, "Student not found.\n")
        return

    sid = student[0]
    result_text.insert(tk.END, f"--- Student Info ---\nID: {sid}\nName: {student[1]}\nClass: {student[2]}\nRoll No: {student[3]}\n")

    result_text.insert(tk.END, "\n--- Attendance ---\n")
    for date, status in get_attendance(sid):
        result_text.insert(tk.END, f"{date}: {status}\n")

    result_text.insert(tk.END, "\n--- Grades ---\n")
    for subj, grade in get_grades(sid):
        result_text.insert(tk.END, f"{subj}: {grade}\n")

    result_text.insert(tk.END, "\n--- Messages ---\n")
    for msg, snd in get_messages(sid):
        result_text.insert(tk.END, f"{snd}: {msg}\n")

# ===== Layout Sections =====

notebook = tk.Frame(root)
notebook.pack(pady=10)

# -------------------- Add Student --------------------
tk.Label(notebook, text="Add Student").grid(row=0, column=0, columnspan=2)
tk.Label(notebook, text="Student ID").grid(row=0, column=0, sticky="w")
id_entry = tk.Entry(notebook)
id_entry.grid(row=0, column=1, pady=2, sticky="ew")

tk.Label(notebook, text="Name").grid(row=1, column=0)
name_entry = tk.Entry(notebook)
name_entry.grid(row=1, column=1)

tk.Label(notebook, text="Class").grid(row=2, column=0)
class_entry = tk.Entry(notebook)
class_entry.grid(row=2, column=1)

tk.Label(notebook, text="Roll No").grid(row=3, column=0)
roll_entry = tk.Entry(notebook)
roll_entry.grid(row=3, column=1)

tk.Button(notebook, text="Add Student", command=add_student).grid(row=4, column=0, columnspan=2, pady=5)

# -------------------- Attendance --------------------
tk.Label(notebook, text="Mark Attendance").grid(row=0, column=2, columnspan=2, padx=20)

tk.Label(notebook, text="Name").grid(row=1, column=2)
att_name_entry = tk.Entry(notebook)
att_name_entry.grid(row=1, column=3)

tk.Label(notebook, text="Date (YYYY-MM-DD)").grid(row=2, column=2)
att_date_entry = tk.Entry(notebook)
att_date_entry.grid(row=2, column=3)

tk.Label(notebook, text="Status (Present/Absent)").grid(row=3, column=2)
status_entry = tk.Entry(notebook)
status_entry.grid(row=3, column=3)

tk.Button(notebook, text="Mark Attendance", command=mark_attendance_gui).grid(row=4, column=2, columnspan=2)

# -------------------- Grades --------------------
tk.Label(notebook, text="Record Grades").grid(row=5, column=0, columnspan=2)

tk.Label(notebook, text="Name").grid(row=6, column=0)
grade_name_entry = tk.Entry(notebook)
grade_name_entry.grid(row=6, column=1)

tk.Label(notebook, text="Subject").grid(row=7, column=0)
subject_entry = tk.Entry(notebook)
subject_entry.grid(row=7, column=1)

tk.Label(notebook, text="Grade").grid(row=8, column=0)
grade_entry = tk.Entry(notebook)
grade_entry.grid(row=8, column=1)

tk.Button(notebook, text="Record Grade", command=record_grades_gui).grid(row=9, column=0, columnspan=2, pady=5)

# -------------------- Messaging --------------------
tk.Label(notebook, text="Send Message").grid(row=5, column=2, columnspan=2)

tk.Label(notebook, text="Name").grid(row=6, column=2)
msg_name_entry = tk.Entry(notebook)
msg_name_entry.grid(row=6, column=3)

tk.Label(notebook, text="Sender (Teacher/Parent)").grid(row=7, column=2)
sender_entry = tk.Entry(notebook)
sender_entry.grid(row=7, column=3)

tk.Label(notebook, text="Message").grid(row=8, column=2)
msg_entry = tk.Entry(notebook, width=30)
msg_entry.grid(row=8, column=3)

tk.Button(notebook, text="Send Message", command=send_msg_gui).grid(row=9, column=2, columnspan=2, pady=5)

# -------------------- Search Student --------------------
tk.Label(root, text="Search Student by Name").pack()
search_name_entry = tk.Entry(root, font=("Arial", 12), width=40)
search_name_entry.pack()
tk.Button(root, text="Search", command=search_student).pack(pady=5)

result_text = tk.Text(root, height=15, width=90, font=("Consolas", 10))
result_text.pack(pady=10)

root.mainloop()
