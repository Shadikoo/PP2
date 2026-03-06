class Student:
    university = "AITU"   # class variable

    def __init__(self, name):
        self.name = name  # instance variable
s1 = Student("Anna")
s2 = Student("Tom")

print(s1.university)
print(s2.university)


class User:
    count = 0

    def __init__(self):
        User.count += 1
u1 = User()
u2 = User()
print(User.count)  # 2
