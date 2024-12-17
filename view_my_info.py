from tkinter import Label

def view_my_stu_info(container, student):
    # Clear the container to avoid stacking widgets
    for widget in container.winfo_children():
        widget.destroy()

    # Heading
    Label(container, text="My Information", font=("Century Gothic", 20), bg="white", pady=10).grid(
        row=0, column=0, columnspan=2, sticky="nsew"
    )

    # Display the student's information
    if student:
        student_info = [
            ("ID", student.getIDnum()),
            ("Full Name", f"{student.fname} {student.lname}"),
            ("Age", student.age),
            ("Email", student.email),
            ("Phone", student.phone),
        ]

        for i, (label, value) in enumerate(student_info, start=1):
            Label(container, text=f"{label}:", font=("Century Gothic", 14), bg="white", anchor="w").grid(
                row=i, column=0, sticky="w", padx=20, pady=5
            )
            Label(container, text=value, font=("Century Gothic", 14), bg="white", anchor="w").grid(
                row=i, column=1, sticky="w", padx=20, pady=5
            )
    else:
        Label(container, text="No student is logged in.", font=("Century Gothic", 14), bg="white", fg="red").grid(
            row=1, column=0, columnspan=2, pady=20
        )