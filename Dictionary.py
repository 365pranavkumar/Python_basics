student = {
    1 : "Pranav",
    2 : "Kumar",
    3 : "Aggarwal"

}
print(student[2])
print(1 in student)
print(4 in student)
print(student.get(5,"Value not found"))
values=student.items()
print(values)
for x in values:
    print(x)
    print(x[0])
    print(x[1])

#Tuples - these are same as list just with diff that they cant be modified
tuple = (1,2,3,4)
print(tuple)