from tkinter import *

def search_other_stu_info(container, students):
    for widget in container.winfo_children():
        widget.destroy()

    Label(container, text="Search Student Info", font=("Century Gothic", 16), bg="gray").pack(pady=10)

    Label(container, text="Enter Student ID:", font=("Century Gothic", 14), bg="gray").pack(pady=5)
    student_id_var = StringVar()
    Entry(container, textvariable=student_id_var, font=("Century Gothic", 14), width=30).pack(pady=5)

    result_label = Label(container, text="", font=("Century Gothic", 14), bg="gray", fg="black", wraplength=600, justify="left")
    result_label.pack(pady=20)

    def perform_search():
        student_id = student_id_var.get().strip()
        other_student = next((s for s in students if s.getIDnum() == student_id), None)

        if other_student:
            full_name = other_student.FullName()
            result_label.config(
                text=f"Name: {full_name}\n"
                     f"ID: {other_student.getIDnum()}\n"
                     f"Email: {other_student.getEmail()}\n"
                     f"Phone: {other_student.getPhoneNum()}",
                fg="black")
        else:
            result_label.config(
                text="Student not found! Please check the ID number and try again.",
                fg="red")

    Button(container, text="Search", font=("Century Gothic", 14), command=perform_search).pack(pady=10)
