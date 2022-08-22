try:
    import os
    os.system("title " + "Roblox Fee Calculator,   Made By $$ Easy#3574,   Github: https://github.com/vlxnehrs")
except:
    pass
def calc():
    while True:
        while True:
            try:
                e = input("Enter Amount Of Robux: ")
                e = float(e)
                break
            except:
                print("Enter A Valid Choice")
        op = 3 / 10
        r =  op * float(e)
        print("Fee: " + str(r))
        print("")
        h = float(e) - r
        print("Owner Will Get: " + str(h))
        print("")
        j = float(e) + float(r)
        print("If Want No Fee Need Pay: " +  str(j))
        input("")
        clear()
def clear():
    try:
        import os
        os.system("cls")
    except:
        pass
calc()
