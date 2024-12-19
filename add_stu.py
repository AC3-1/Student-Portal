from student import StudentInfo
import os
from tkinter import *
import tkinter.messagebox

STUDENT_FILE = "students.txt"

class AddStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def add_stu(self, fname, lname, age, Idnum, password, email, phone):
        student = StudentInfo()
        student.setFirstName(fname)
        student.setLastName(lname)
        student.setAge(age)
        student.setIDnum(Idnum)
        student.setPassword(password)
        student.setEmail(email)
        student.setPhoneNum(phone)

        self.student_data.append(student)
        self.add_student_to_file(student)
        print(f"Student {student.FullName()} added successfully")
        self.add_student_to_file(student)

    def add_stu_via_input(self):
            while True:
                fname = input("Enter first name: ")
                lname = input("Enter last name: ")
                age = input("Enter age: ")

                while True:
                    Idnum = input("Enter ID number: ")
                    if any(student.getIDnum() == Idnum for student in self.student_data):
                        print("ID number already taken. Enter another unique ID number.")
                    else:
                        break

                password = input("Enter password: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")

                new_student = StudentInfo(fname, lname, age, Idnum, password, email, phone)
                self.student_data.append(new_student)
                self.add_student_to_file(new_student)
                print("Student added successfully!")

                add_another = input("Do you want to add another student? [Y/N]: ").strip().lower()
                if add_another != 'y':
                    break

    def show_reg_ui(self, reg_frame):
        self.lblError = Label(reg_frame, text="", font=("Century Gothic", 12), fg="red", bg="gray")
        self.lblError.grid(row=1, column=0, columnspan=2)
        self.reg_lbl_txt = ["First Name", "Last Name", "Age", "ID Number", "Password", "Email", "Phone Number"]
        self.reg_entries = []
        for i in range(len(self.reg_lbl_txt)):
            Label(reg_frame, text=self.reg_lbl_txt[i], font=("Century Gothic", 14), width=14, anchor="e", bg="gray").grid(row=i+2, column=0)
            self.reg_entries.append(Entry(reg_frame, font=("Century Gothic", 14)))
            self.reg_entries[i].grid(row=i+2, column=1)
        reg_btn = Button(reg_frame, text="Register", font=("Century Gothic", 14), command=self.check_entry)
        reg_btn.grid(columnspan=4)
            
    def check_entry(self):
        errors = []
        for i in range(len(self.reg_entries)):
            if self.reg_entries[i].get() == "":
                errors.append(f"{self.reg_lbl_txt[i]} is required.\n")
            if not errors:
                self.add_stu(self.reg_entries[0].get(), self.reg_entries[1].get(), self.reg_entries[2].get(), self.reg_entries[3].get(), self.reg_entries[4].get(), self.reg_entries[5].get(), self.reg_entries[6].get())
                tkinter.messagebox.showinfo("Success", "Student added successfully!")
                self.reset_error()
            else:
                self.lblError.config(text="".join(errors))
                
    def reset_txt(self):
        for i in range(len(self.reg_entries)):
            self.reg_entries[i].delete(0, END)
        
    def reset_error(self):
        self.lblError.config(text="")
        self.reset_txt()
        
    def add_student_to_file(self, student):
        with open(STUDENT_FILE, 'a') as file:
            file.write(f"{student.fname}, {student.lname}, {student.age}, {student.Idnum}, {student.password}, {student.email}, {student.phone}\n")