print("enter an integer")
inp = int(input())

print("enter 1 or 0 zero")
trf = bool(int(input()))
i=1

if (trf == True):
    for i in range(inp + 1):
        print("*" * i)
        i = i + 1
elif (trf == False):
    for i in range(inp + 1):
        print("*" * (inp - i))
        i = i + 1
