from tkinter import *

def view_all_stu_info_gui(container, students):
    for widget in container.winfo_children():
        widget.destroy()

    Label(container, text="All Students Information", font=("Century Gothic", 16), bg="gray").pack(pady=10)

    if not students:
        Label(container, text="No students in the system.", font=("Century Gothic", 14), bg="gray", fg="red").pack(pady=20)
    else:
        for student in students:
            student_info = (
                f"Name: {student.FullName()}\n"
                f"ID: {student.getIDnum()}\n"
                f"Age: {student.getAge()}\n"
                f"Email: {student.getEmail()}\n"
                f"Phone: {student.getPhoneNum()}"
            )
            student_label = Label(container, text=student_info, font=("Century Gothic", 14), bg="gray", justify="left", wraplength=600)
            student_label.pack(pady=10)
            Label(container, text="-"*30, font=("Century Gothic", 14), bg="gray").pack()