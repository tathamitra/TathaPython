print("Enter number of apples")
apples = int(input())

print("Enter the max and Min seperated by comma ")
maxmin = input()
max= int(maxmin.split(",")[0])
min = int(maxmin.split(",")[1])
print(max,min)
if max == min :
    if apples % max == 0:
        print(f"your numbers are same i.e {max} and is divisible by {apples}")
    else:
        print(f"your numbers are same i.e {max} and is not divisible by {apples}")
elif min>max:
      print(f"your minimum number {min} is greater that {max}")
else:
    for i in range(min,max+1):
       if apples%i == 0:
           print(f"{i} is a divisor of {apples}")
       else :
           print(f"{i} is not divisor of {apples}")
