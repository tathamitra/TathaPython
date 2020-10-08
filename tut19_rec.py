
print("Enter a number")
inp = int(input())

#factorial using iterat0ive
c = 1
def fact_inter(inp):
    c=1
    for i in range(inp):
        c=c*(i+1)
    print("The iterative factorial is:",c)

#factorial using iterat0ive
def fact_recursive(inp):
    if inp ==1:
        return  inp
    else:
     return  inp*fact_recursive(inp -1)


print(fact_inter(inp))
print("The iterative factorial is:",fact_recursive(inp))

#fibonacci number of nth element

