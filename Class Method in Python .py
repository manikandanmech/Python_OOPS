
                    #Class Method in Python

class Student:
    name = "Manikandan"
    age = 20

    def printall():
        print("Name : ", Student.name)
        print("Age  : ", Student.age)


Student.printall()
print(Student.__dict__)

print(getattr(Student, "printall"))
getattr(Student, "printall")()

Student.__dict__['printall']()