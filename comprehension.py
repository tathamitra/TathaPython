# ls=[]
#
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
# print("all numbers till 100 divisible by 3",ls)

ls = [i for i in range(100)]
print("all numbers till 100",ls)

ls = [i for i in range(100) if i%3 == 0]
print("all numbers till 100 divisible by 3",ls)