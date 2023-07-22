              #Class Method Decorator in Python
class student:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def printDetail(self):
        print("Name  : ", self.name, "  Age : ", self.age)

    @classmethod
    def total(cls):
        return cls.count


o = student("mani", 20)
o.printDetail()
a = student("Raj", 22)
a.printDetail()

print("Total Admission :", student.total())
print("Total Admission :", o.total())