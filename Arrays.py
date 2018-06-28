list1=["Mango","Apple","Banana","Guava"]
print(list1)
list1[3]="Orange"
print("\n Guava is updated to Orange:")
print(list1)

#updating item from array on user's input
x=int(input("Enter index to be changed ranging from 0-3"))
y=input("Enter new string")
list1[x]=y
print(list1)

#Adding two Strings
print("\n\n Adding two lists: ")
list2=[1,2,3]
list3=list1+list2
print(list3)

#IN operation
print("\n\n IN OPERATION")
print("Apple" in list1)

#multiply operation
print("\n\n Multiply two lists")
list4=list1*3
print(list4)

# Append function
print("\n\n Append function:")
list1.append("kiwi")
print(list1)
#Appending two lists
list1.append(list2)
print(list1)

# Length function
print("\n\n Length Function")
print(len(list1))

# Insert Operation
print("\n\n Insert function")
list1.insert(1,"Cheeku")
print(list1)



#Index function
z=str(input("Enter fruit to be searched"))
print(list1.index(z))

#Range Function
#list5=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#print(list5)
list6=list(range(10))
print(list6)
list7=list(range(2,11))
print(list7)
list8=list(range(0,31,2))
print(list8)

#deleting something from a list
list10=["mango","banana","Apple","cheeku"]
list10.remove("Apple")
print(list10)


#2-D Lists


