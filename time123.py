import  time

initial = time.time()
print(initial)

for i in range(45):
    print (i)
final = time.time()
print(final)

print("time taken by this loop ", time.time()-initial)