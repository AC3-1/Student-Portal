from tkinter import *

def view_all_stu_info_gui(parent_frame, students):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    Label(parent_frame, text="All Students Information", font=("Century Gothic", 16), bg="white").pack(pady=10)

    if not students:
        Label(parent_frame, text="No students in the system.", font=("Century Gothic", 14), bg="white", fg="red").pack(pady=20)
    else:
        for student in students:
            student_info = (
                f"Name: {student.FullName()}\n"
                f"ID: {student.getIDnum()}\n"
                f"Age: {student.getAge()}\n"
                f"Email: {student.getEmail()}\n"
                f"Phone: {student.getPhoneNum()}"
            )
            student_label = Label(parent_frame, text=student_info, font=("Century Gothic", 14), bg="white", justify="left", wraplength=600)
            student_label.pack(pady=10)
            Label(parent_frame, text="-"*30, font=("Century Gothic", 14), bg="white").pack()


