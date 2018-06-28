def add(x, y=9):
    c = x + y
    print(c)

add(2)

#global variables

a=10
def add(b):  #b is local variable
    d=a+b
    print(d)

def sub(b):
    f=a-b
    print(f)

add(5)
sub(5)

def names(message,mess):
    print(message)
    print(mess)

names("hello","world")
names(mess="world",message="hello")

def names(*names):
    print(names)
    for p in names:
        print(p)

names("a","b","c","d")

def add1(x,y):
    c=x+y
    return(c)

abc=add1(234,456)
print(abc)

num=int(input("Enter the number you want factorial of: "))
fact = 1

for j in range(1,num+1):
    fact=fact*j

print(fact)

#Factorial using recursion

def fac(n):

    if n == 1 :
        return n;
    else:
        return n*fac(n-1)


num=int(input("Enter the number you want factorial of: "))
if num<0:
    print("Sorry factorial doesnt exist")
elif num==0:
    print("Factorial is 1")
else:
    print("Factorial is ",fac(num))



