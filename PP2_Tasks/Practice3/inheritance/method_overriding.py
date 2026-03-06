# Parent class Animal
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class Dog that inherits from Animal
class Dog(Animal):
    def speak(self):
        print("Dog barks")  # Override the parent class method

# Create an instance of Dog class
d = Dog()
# Call the speak method
d.speak()  # Output: "Dog barks"