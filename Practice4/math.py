#1
import math

degrees = float(input("Input degree: "))
radians = degrees * (math.pi / 180)
print(f"Output radian: {radians:.6f}")

#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2
print(f"Expected Output: {area}")

#3
import math

n = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = (n * side_length ** 2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:.0f}")

#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print(f"Expected Output: {area}")