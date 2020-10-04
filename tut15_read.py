# I/O basics
f = open("test.txt")
content = f.read()
print(content)
f.close()
###########################
f = open("test.txt")
content = f.read(3)
print(content)
f.close()

###########################
f = open("test.txt")
for line in f:
 print(line)
f.close()

###########################
f = open("test.txt")
content = f.readline()
print(content)
f.close()
###########################
f = open("test.txt")
content = f.readlines()
print(content)
f.close()