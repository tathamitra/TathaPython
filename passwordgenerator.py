import random
import string

def password_generator():
    a= random.choice(string.ascii_uppercase)
    b= random.choice(string.ascii_lowercase)
    c = random.randint(0,9)
    l1= ["@","3","$","%","^","&","*","(",")"]
    d= random.choice(l1)
    e= random.randint(0,9)
    f= random.choice(string.ascii_uppercase)
    g = random.choice(l1)
    h= random.choice(string.ascii_lowercase)

    passwordlist = [a,b,c,d,e,f,g,h]
    random.shuffle(passwordlist)
    password=''.join(map(str, passwordlist))

    return  password

if __name__ == '__main__':
    g = password_generator()
    print(f"You random password generated is : {g} ")
