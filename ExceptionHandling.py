def div(a, b):
        try:
            c = a/b
            print(c)
        except ZeroDivisionError:
            print("Enter the numbers carefully")

print(div(2, 3))

while True:
    try:
        x=input("..Please Enter Number")
        x=int(x)
        print(x)
        break
    except ValueError:
        print("Please Enter a number")

