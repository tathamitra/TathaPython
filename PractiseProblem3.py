
print("print the size of list")
size = int(input())

l1 = []


for i in range(size):
    print("Enter values in list")
    num = int(input())
    l1.append(num)

print("original list is",l1)
A1 = l1[:]
A1.reverse()
print(" reversed list first process ",A1)
A2=l1[::-1]
print(" reversed list second process ",A2)

for i in range(size):
    l1[i]=l1[size-i]
print("third process",l1)