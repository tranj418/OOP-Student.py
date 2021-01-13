# OOP-Student.py
OOP for student list


student1 = ["Jim", 24, "Junior", "Information Systems"]
student2 = ["Jamal", 25, "Junior", "Marine Biology"]

class StudentList:

    alias = "Explorers"

    def __init__(self, name, age, school_year, major, hobby):
        #The below are Instance Attributes!
        self.name = name
        self.age = age
        self.school_year = school_year
        self.major = major
        self.hobby = hobby
    
    def action(self):
        print(f"{self.name} is currently a student in college and they are {self.age} years old.")

    def information(self):
        information = f"name = {self.name}, age = {self.age}, school year = {self.school_year}, major = {self.major}"
        return information

    @staticmethod
    #Will still work, even through we did not include the argument "self"
    #Since we have the static method
    def credits(credit):
        if credit > 60:
            print("you may register for classes early.")
        else:
            print("you must await for your register date.")
    
    def __eq__(self, other):#must include self, and another variable that it is being compared to, i.e. other.
        return self.name == other.name and self.age == other.age

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, school year = {self.school_year}, major = {self.major}"
        return information




student1 = StudentList("Jim", 24, "Junior", "Information Systems", "traveling")
student2 = StudentList("Jamal", 25, "Junior", "Marine Biology", "traveling")
student3 = StudentList("Jamal", 25, "Junior", "Marine Biology", "traveling")


#print(student1.name, student1.age)
#print(student2.name, student2.age)

#print(student1.hobby) #Experiment, added in hobby to the parameters after they were already set

#student1.action()
#student2.action()

#print(StudentList.alias)

#print(student1.credits(70)) 
#print(student2.credits(80))

#print(student2.name == student3.name)

print(student1.information())
