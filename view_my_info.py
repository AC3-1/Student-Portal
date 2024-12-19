from tkinter import Label

def view_my_stu_info(container, student):
    for widget in container.winfo_children():
        widget.destroy()
        
    Label(container, text="My Information", font=("Century Gothic", 20), bg="gray", pady=10).grid(
        row=0, column=0, columnspan=2, sticky="nsew")

    if student:
        student_info = [
            ("ID", student.getIDnum()),
            ("Full Name", f"{student.fname} {student.lname}"),
            ("Age", student.age),
            ("Email", student.email),
            ("Phone", student.phone),
        ]

        for i, (label, value) in enumerate(student_info, start=1):
            Label(container, text=f"{label}:", font=("Century Gothic", 14), bg="gray", anchor="w", height=5, width=5).grid(
                row=i, column=0, sticky="w", padx=20, pady=5)
            Label(container, text=value, font=("Century Gothic", 14), bg="gray", anchor="w").grid(
                row=i, column=1, sticky="w", padx=20, pady=5)
    else:
        Label(container, text="No student is logged in.", font=("Century Gothic", 14), bg="gray", fg="red").grid(
            row=1, column=0, columnspan=2, pady=20)
