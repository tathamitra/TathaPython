l = 34

def funtosh():
    l =54
    def crook():
        global l
        l= 67
    print("before calling crook the value of l", l )
    crook()
    print("after calling crook the value of l", l)
print(l)
funtosh()
print(l)

