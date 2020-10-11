
def fun(normal, * args, ** kwargs):
    print (normal)
    print ("the teacher of this class is: ",args[0])
    print("the students of this class are:")
    for item in args:
        print(item)
    print("The heroes of this class are:")
    for key,value in kwargs.items():
        print(f"{key} is the {value} of the class")

sample = ["ram","shyam","jadu","madhu"]
sample1 = {"ram": "Monitor", "shyam": "coordinator"}
test = "Welcome to the class"
fun(test, *sample, **sample1)