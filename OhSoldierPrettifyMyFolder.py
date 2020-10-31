import os
def soldier(path,exceptfile,format):
    a = 0
    f = open(exceptfile, 'r')
    info = f.read()
    excpt = info.split()
    print("except filecontent",excpt)
    if os.path.isdir(path):
        os.chdir(path)
        l1 = os.listdir()
        print(l1)
        for i in l1:
#for file not in except.txt, capitalize the first letter
            if i not in excpt:
              d = i.capitalize()
              os.rename(i, d)
#  change name of specific format to sequential 1-100
            if i.endswith(format) :
                a = a + 1
                os.rename(i,f"{a}.{format}")
    else:
        print("path is invalid")
    return path

soldier("D:/Users/Soldier","soldir.txt","jpg")
