from add_stu import AddStudent
from aload_students import load_students_from_file, file_wipe, STUDENT_FILE
from student import StudentInfo
from search_studentinfo import search_other_stu_info
from print_allstuinfo import view_all_stu_info
from view_my_info import view_my_stu_info
import os

def clear():
    os.system('cls')

def student_portal():
    file_wipe(STUDENT_FILE)
    student_list = load_students_from_file()
    addstud = AddStudent(student_list)
    if not any(s.getIDnum() == "admin" for s in student_list):
        addstud.add_stu("ADMIN", "", "27", "admin", "admin","admin@gmail.com", "09181818181818")
    while True:
        print("Welcome to the student portal!")
        user_id = input("Enter ID Number: ")
        clear()

        if user_id.lower() == 'exit':
            print("Exiting the student portal. Goodbye!")
            break

        student = next((s for s in student_list if s.getIDnum() == user_id), None)

        if student:
            while True:
                print(f"\nWelcome, {student.lname}!\n1. View my student info \n2. View another student's info \n3. Add new student\n4. View all student info \n5. Exit")
                choice = input("\nEnter your choice: ")
                clear()
                if choice == '1':
                    view_my_stu_info(student)
                    input(" ")
                    clear()
                elif choice == '2':
                    search_other_stu_info(student_list)
                elif choice == '3':
                    addstud.add_stu_via_input()
                    student_list = load_students_from_file()
                elif choice == '4':
                    view_all_stu_info(student_list)
                    input(" ")
                    clear()
                elif choice == '5':
                    print("Exiting the student portal!")
                    exit()
                else:
                    print("\nInvalid choice!")

        else:
            print("\nStudent not found! Please check the ID number and try again.")

student_portal()