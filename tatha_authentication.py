
#password creation and authentication
class credential():
    creds = {}

    def __init__(self,choice):
        self.choice = choice


    def login(self):
        print()
        print("Enter your username")
        usrnm = input()
        print("Enter your password")
        pwd = input()
        f = open("creds.txt", 'r')
        info = f.read()
        info = info.split()
        if usrnm in info:
            index = info.index(usrnm) + 1
            usr_password = info[index]
            if usr_password == pwd:
                print("Welcome Back, " + usrnm)
            else:
                print("Password entered is wrong")
        else:
            print("Name not found. Please Sign Up.")


    def recheckcreatedlogin(self):
        print("Let us see if you remember")
        print("re-Enter your username")
        usrnm = input()
        print("re-Enter your password")
        pwd = input()
        if usrnm not in self.creds.keys():
            print("Username does not match the previous one")
        elif pwd not in self.creds.values():
            print("password does not match the previous one")
        else:
            for key1, value1 in self.creds.items():
                if self.creds.get(usrnm) == pwd:
                    print("you are confirmed!!!")
                    with open("creds.txt", "a") as f:
                        f.write(f"{usrnm} {pwd}\n")
                else:
                    print("Credentials do not match")

    def createcredentials(self):
        print("set your username")
        usrnm = input()
        print("set your password")
        pwd = input()


        self.creds[usrnm] = pwd

        # for keys, values in self.creds.items():
        #     print("the keys are ",keys)
        #     print("the values are ",values
        #     )


def main():

 while True:
     print("Enter 1 to  login and 2 create login")
     choice = int(input())
     newcreds = credential(choice)

     if choice == 1:
        newcreds.login()
     elif choice == 2:
         newcreds.createcredentials()
         newcreds.recheckcreatedlogin()


if __name__ == "__main__":
    main()