import random

HomeScreen = 0
while HomeScreen == 0:
    cevap1 = input("İşlemler: \n1.Şifre Oluştur\n2.Sifrelerime bak\n")
    if cevap1 == "1":
        Dx = 0
        while Dx == 0:
            cevap2 = input("Şifrenizin Başlığı: ")
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
            print("Yeni şifre: "+fLetter)
            dosya.write(cevap2+": "+fLetter+"\n")
            dosya.close()
            cevap3 = input("Çıkmak için x: \nİşlemlere devam etmek için a:")
            if cevap3 == "x":
                print("Çıkış yapılıyor")
                Dx = 1
                HomeScreen = 1
            elif cevap3 == "a":
                Dx = 1
    elif cevap1 == "2":
        with open("passwords.txt","r") as dosya:
            for satir in dosya:
                print(satir)    
        cevap4 = input("Çıkmak için x: \nİşlemlere devam etmek için a:")
        if cevap4 == "x":
            print("Çıkış yapılıyor")
            Dx = 1
            HomeScreen = 1
        elif cevap4 == "a":
            Dx = 1