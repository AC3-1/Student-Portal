from tkinter import *
from functools import partial
from add_stu import AddStudent
from aload_students import load_students_from_file, file_wipe, STUDENT_FILE
from student import StudentInfo
from search_studentinfo import search_other_stu_info
from print_allstuinfo import view_all_stu_info_gui
from view_my_info import view_my_stu_info

win = Tk()
win.title("Student Portal")
win.geometry(f"1280x800+{(win.winfo_screenwidth() - 1280) // 2}+{(win.winfo_screenheight() - 800) // 2}")

btns, containers = [], []
student_list = load_students_from_file()
addstud = AddStudent(student_list)

if not any(s.getIDnum() == "admin" for s in student_list):
    addstud.add_stu("ADMIN", "", "27", "admin", "admin", "admin@gmail.com", "09181818181818")

def validate_login(username, password):
    global logged_in_student
    user_id = username.get()
    user_pass = password.get()
    
    student = next((s for s in student_list if s.getIDnum() == user_id), None)

    if student and student.password == user_pass:
        logged_in_student = student
        login_contain.pack_forget()
        menu_contain.pack(side="left", fill="y")
        content_contain.pack(side="left", fill="x")
        content_label.config(text=f"Welcome, {student.fname} {student.lname}!")
    else:
        login_error_label.config(text="Invalid username or password")

def Exit_Program():
    win.destroy()

def open_frame(frame_open, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped():
            close[i].pack_forget()
    frame_open.pack(side="left", fill="x")
    

# Login Screen
login_contain = Frame(win, bg="white")
for i in range(11):
    login_contain.grid_rowconfigure(i, weight=1)
    login_contain.grid_columnconfigure(i, weight=1)

Label(login_contain, text="Login", font=("Century Gothic", 20), bg="white").grid(row=1, column=4, columnspan=2, pady=10, sticky="nsew")
Label(login_contain, text="Student ID:", font=("Century Gothic", 14), bg="white").grid(row=3, column=4, padx=10, pady=10, sticky="nsew")
Label(login_contain, text="Password:", font=("Century Gothic", 14), bg="white").grid(row=5, column=4, padx=10, pady=10, sticky="nsew")

username = StringVar()
password = StringVar()

Entry(login_contain, textvariable=username, font=("Century Gothic", 14)).grid(row=3, column=5, padx=10, pady=10, sticky="ew")
Entry(login_contain, textvariable=password, font=("Century Gothic", 14), show="*").grid(row=5, column=5, padx=10, pady=10, sticky="ew")

login_error_label = Label(login_contain, text="", font=("Century Gothic", 12), fg="red", bg="white")
login_error_label.grid(row=3, column=0, columnspan=2)

Button(login_contain, text="Login", font=("Century Gothic", 14), command=partial(validate_login, username, password)).grid(row=8, column=4, columnspan=2, pady=20, sticky="nsew")

login_contain.pack(fill="both", expand=True)

# Menu Screen
menu_contain = Frame(win, bg="black")
btn_txt = ["View My Info", "View Another Student's Info", "Add New Student", "View All Students", "Exit"]

Label(menu_contain, text="Student Portal", font=("Century Gothic", 20), bg="black", fg="white").grid(row=0, column=0, pady=10)

# Content Area
content_contain = Frame(win, bg="white")
content_label = Label(content_contain, text="Main Menu", font=("Century Gothic", 20), bg="black", fg="white", anchor="n")
content_label.pack(fill="x", pady=5)

# Frame for content
for i in range(len(btn_txt)-1):
    containers.append(Frame(content_contain, bg="gray"))
    Label(containers[i], width=79, text=btn_txt[i], font=("Century Gothic", 16), bg="white", pady=20, anchor="center").grid(row=0, column=0, columnspan=4)

funcs = [partial(open_frame, containers[0], [containers[1], containers[2], containers[3]]),
         partial(open_frame, containers[1], [containers[0], containers[2], containers[3]]),
         partial(open_frame, containers[2], [containers[1], containers[0], containers[3]]),
         partial(open_frame, containers[3], [containers[1], containers[2], containers[0]]),
         Exit_Program]

for i, txt in enumerate(btn_txt):
    btn = Button(menu_contain, text=txt, font=("Century Gothic", 14), width=30, bg="white", command=funcs[i])
    btn.grid(row=i+1, column=0, pady=5)
    if i == 4:
        btn.grid(pady=509)

    
for i in range(len(btns)):
    btns[i.config(command=funcs[i])]

addstud.show_reg_ui(containers[2])
view_my_stu_info(containers[0], student_list[0])
search_other_stu_info(containers[1], student_list)
view_all_stu_info_gui(containers[3], student_list)

win.mainloop()