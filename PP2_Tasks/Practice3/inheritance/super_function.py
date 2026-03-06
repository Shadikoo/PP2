class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

# Example 1: Basic inheritance with super()
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# Example 2: Adding a fixed property
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

# Example 3: Adding a parameter for the property
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

# Example 4: Adding a method
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Creating objects
x = Student("Mike", "Olsen", 2019)
x.printname()    # From Person class
x.welcome()      # From Student class
# Output:
# Mike Olsen
# Welcome Mike Olsen to the class of 2019