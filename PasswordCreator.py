import random

HomeScreen = 0
while HomeScreen == 0:
    cevap1 = input("Transactions: \n1.Password Create\n2.Check your passwords\n")
    if cevap1 == "1":
        Dx = 0
        while Dx == 0:
            cevap2 = input("Your Password Title: ")
            dosya = open("passwords.txt","a",encoding="utf-8")
            pLetters = []
            password = input("Password: ")
            pLength = len(password)
            for i in range(0,pLength):
                pLetters.append(password[i])
            random.shuffle(pLetters)
            i = 0
            fLetter = pLetters[0]
            while i+1 != len(pLetters):
                newPassword = fLetter + pLetters[i+1]
                i = i + 1
                fLetter = newPassword
            print("New Password: "+fLetter)
            dosya.write(cevap2+": "+fLetter+"\n")
            dosya.close()
            cevap3 = input("'x' to exit: \nTo continue operations 'a':")
            if cevap3 == "x":
                print("exit is in progress")
                Dx = 1
                HomeScreen = 1
            elif cevap3 == "a":
                Dx = 1
    elif cevap1 == "2":
        try: 
            with open("passwords.txt","r") as dosya:
                for satir in dosya:
                    print(satir)
        except:
            print("An error occurred while opening the file. The file does not exist or is unreadable.")
        cevap4 = input("'x' to exit: \nto continue operations 'a'")
        if cevap4 == "x":
            print("exit is in progress")
            Dx = 1
            HomeScreen = 1
        elif cevap4 == "a":
            Dx = 1