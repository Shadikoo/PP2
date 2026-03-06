# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    pass

# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() function to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        # Call the parent class constructor
        Person.__init__(self, fname, lname)

# Or better, using super() (more modern approach):
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)