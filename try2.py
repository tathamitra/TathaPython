f1 = open("test.txt")

try:
 f = open("tree.txt")

except Exception as e:
    print(e)
else:
    print("this will run if except is not running")
finally:
    f1.close()
    print("run this anyway")
