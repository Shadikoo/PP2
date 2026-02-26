#1 
def square_generator(N):
    for i in range(1, N + 1):
        yield i * i

N = int(input("Enter N: "))
for square in square_generator(N):
    print(square)

#2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
print(','.join(map(str, even_numbers(n))))

#3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
for num in divisible_by_3_and_4(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter a: "))
b = int(input("Enter b: "))
for value in squares(a, b):
    print(value)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter n: "))
for num in countdown(n):
    print(num)