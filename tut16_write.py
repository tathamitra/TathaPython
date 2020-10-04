###########################
f = open("test1.txt" , "w")
content = f.write("New Chance")
print(content)
f.close()
###########################
f = open("test1.txt" , "a")
content = f.write("\n New morning")
print(content)
f.close()

###########################
f = open("test1.txt" , "r+")
f.read()
content = f.write("\n New day")
f.close()