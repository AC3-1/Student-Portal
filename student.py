class StudentInfo:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.age = ""
        self.Idnum = ""
        self.password = ""
        self.email = ""
        self.phone = ""

    def setFirstName(self, fname):
        self.fname = fname

    def setLastName(self, lname):
        self.lname = lname

    def setAge(self, age):
        self.age = age

    def setIDnum(self, Idnum):
        self.Idnum = Idnum

    def setPassword(self, password):
        self.password = password

    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, phone):
        self.phone = phone

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname

    def getAge(self):
        return self.age

    def getIDnum(self):
        return self.Idnum

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.phone

    def FullName(self):
        return f"{self.fname} {self.lname}"

    def __str__(self):
        return f"\nName      : {self.FullName()} \nAge       : {self.age} \nID Number : {self.Idnum} \nPassword  : {self.password} \nEmail     : {self.email} \nContact   : {self.phone}"