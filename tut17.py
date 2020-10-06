###########################
f = open("test1.txt")
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(11)
print(f.readline())

f.close()

###################################
with open ("test1.txt") as f:
    a = f.readlines()
    print(a)