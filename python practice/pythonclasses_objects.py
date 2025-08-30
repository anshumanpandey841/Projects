class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print("Name:", self.name, "age:", self.age)

s1 = Student("Anshuman,", 20)
s1.display_info()
s2 = Student("shukhi,", 21)
s2.display_info()