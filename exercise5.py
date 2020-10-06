print("enter the candidate name press 1 for Harry, 2 For Hamad, 3 For Rohan:")
cnameint = int(input())
print("enter the type 1 for food, 2 For Exercise:")
ctypeint = int(input())
print("enter whether you want to read or write 1 for read 2 for write:")
cactionint = int(input())


if (cnameint == 1):
    if (ctypeint == 1):
      cname = 'Harry_Food.txt'
    elif (ctypeint == 2):
      cname = 'Harry_Exercise.txt'
    else:
      print("Enter valid input_1")

elif (cnameint == 2):
    if (ctypeint == 1):
        cname = 'Hamad_Food.txt'
    elif (ctypeint == 2):
        cname = 'Hamad_Exercise.txt'
    else:
        print("Enter valid input_2")
elif (cnameint == 3):
    if (ctypeint == 1):
        cname = 'Rohan_Food.txt'
    elif (ctypeint == 2):
        cname = 'Rohan_Exercise.txt'
    else:
        print("Enter valid input_3")
else:
    print("wrong input")

def Enterdata(name,userdata,timeofentry):
    f = open(name, "a")
    entry = "\n" + str(timeofentry)  + ("  ") + userdata
    content = f.write(entry)
    f.close()

def readdata(name):
    with open(cname) as f:
        a = f.readlines()
        print(a)

def getdate():
    import datetime
    return str(datetime.datetime.now())

if (cactionint == 1):
    print("enter what you want to enter")
    cdata = input()
    Enterdata(cname, getdate(), cdata)
elif (cactionint == 2):
    readdata(cname)
else:
    print("Enter Valid Input_4")




