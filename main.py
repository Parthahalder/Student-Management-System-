from database import setup_db
from model import *

# Initialize DB
setup_db()
name_input = input("Enter student name to fetch details: ")
if not get_student_by_name(name_input):
    
    enroll_student(1,"Rahul", "10A", 101)
    enroll_student(2,"Bob", "10A", 102)

    # Get student IDs after creation
    students = get_student_by_name(name_input)
    student1_id = students[0][0]
    student2_id = students[1][0]

    mark_attendance(student1_id, "2025-05-27", "Present")
    mark_attendance(student2_id, "2025-05-27", "Absent")

    record_grade(student1_id, "Math", "A")
    record_grade(student2_id, "Math", "B")

    send_message(student1_id, "Your child is doing well in math.", "Teacher")
    send_message(student2_id, "Will look into Bob’s performance.", "Parent")


student = get_student_by_name(name_input)

if student:
    student_id = student[0]
    print(f"\n--- Student Info ---\nID: {student[0]}, Name: {student[1]}, Class: {student[2]}, Roll No: {student[3]}")

    print("\n--- Attendance Records ---")
    attendance = get_attendance(student_id)
    if attendance:
        for date, status in attendance:
            print(f"{date}: {status}")
    else:
        print("No attendance records found.")

    print("\n--- Grades ---")
    grades = get_grades(student_id)
    if grades:
        for subject, grade in grades:
            print(f"{subject}: {grade}")
    else:
        print("No grades recorded.")

    print("\n--- Communication ---")
    messages = get_messages(student_id)
    if messages:
        for message, by in messages:
            print(f"{by}: {message}")
    else:
        print("No messages available.")
else:
    print("Student not found.")