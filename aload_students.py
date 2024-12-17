from student import StudentInfo
import os

STUDENT_FILE = "students.txt"

def file_wipe(file_path):
    with open(file_path, 'w') as file:
        pass

def load_students_from_file():
    students = []
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if len(data) == 6:
                    try:
                        fname, lname, age, Idnum, email, phone = data
                        student = StudentInfo()
                        student.setFirstName(fname)
                        student.setLastName(lname)
                        student.setAge(age)
                        student.setIDnum(Idnum)
                        student.setEmail(email)
                        student.setPhoneNum(phone)
                        students.append(student)
                    except Exception as e:
                        print(f"Error loading student data: {data} | Error: {e}")
                else:
                    print(f"Invalid data format in line: {line}")
    else:
        print("Creating new file....")
        with open(STUDENT_FILE, 'w') as file:
            pass
    
    return students