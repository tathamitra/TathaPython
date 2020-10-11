numbers = ["17","23","34","51"]
# print(numbers[3]+3) #will throw error as numbers are string
l1= list(map(int,numbers))
print(l1[3]+3)