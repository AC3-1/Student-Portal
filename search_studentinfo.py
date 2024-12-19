from tkinter import *

def search_other_stu_info(parent_frame, students):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    Label(parent_frame, text="Search Student Info", font=("Century Gothic", 16), bg="white").pack(pady=10)

    Label(parent_frame, text="Enter Student ID:", font=("Century Gothic", 14), bg="white").pack(pady=5)
    student_id_var = StringVar()
    Entry(parent_frame, textvariable=student_id_var, font=("Century Gothic", 14), width=30).pack(pady=5)

    result_label = Label(parent_frame, text="", font=("Century Gothic", 14), bg="white", fg="black", wraplength=600, justify="left")
    result_label.pack(pady=20)

    def perform_search():
        student_id = student_id_var.get().strip()
        other_student = next((s for s in students if s.getIDnum() == student_id), None)

        if other_student:
            full_name = other_student.FullName()  # Fixed method access
            result_label.config(
                text=f"Name: {full_name}\n"
                     f"ID: {other_student.getIDnum()}\n"
                     f"Email: {other_student.getEmail()}\n"
                     f"Phone: {other_student.getPhoneNum()}",
                fg="black"
            )
        else:
            result_label.config(
                text="Student not found! Please check the ID number and try again.",
                fg="red"
            )

    Button(parent_frame, text="Search", font=("Century Gothic", 14), command=perform_search).pack(pady=10)
