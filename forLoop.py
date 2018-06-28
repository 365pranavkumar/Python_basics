for x in range(0,10):
    print("Pranav")

list1=["Apple","Kiwi","Banana"]
for x in list1:
    print(x)
for y in range(0,len(list1)):
    print(list1[y])

abc=range(0,6)  #Used in cases where range is used multiple times
for a in abc:
    print("I am a programmer")

list2=[]
list3=[]
for b in range(0,101):
    if(b%2==0):
        list2.append(b)
    else:
        list3.append(b)

print(list2)
print(list3)

a=[[1,1,-1],[1,2,0],[-1,0,5]]
sym="Matrix is symmetric"
for i in range(0,3):
    for j in range(0,3):
        if a[i][j]!=a[j][i]:
            sym="Matrix is not symmetric"

print(sym)

# Reverse String

word = input("Pranav Kumar Aggarwal")
for char in range(len(word)-1,-1,-1):
    print(word[char],end="")