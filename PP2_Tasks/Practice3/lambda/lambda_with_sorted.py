x = input()
flag = True
for i in x:
    a = int(i)
    if a % 2 != 0:
        flag = False
        break

if flag :
    print("Valid")
else:
    print("Not valid")