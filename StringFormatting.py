date = ["june ","11 ","2018"]
num = "date:{1}{0}{2}".format(date[0],date[1],date[2])
print(num)
print(date)
print(";".join(date))

print("hello world".replace("hello","hi"))

str = "Pranav kumar aggarwal"
print(str.startswith("Pranav"))
print(str.endswith("al"))
print(str.upper())
print(str.lower())

while True:  #T of true must be uppercase
    name = input("Enter any name")
    print("DO you know Pranav?")
    if name == "Pranav":
        break

print("Thank you")

while True:
    name1=input("Enter your name")
    if name1!= "Kumar":
        continue
    break
print("hello Pranav")

