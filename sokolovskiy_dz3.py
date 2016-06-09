print("SOKOLOVSKIY MATVEY  GROUP: 152. VARIANT 1. HOMEWORK 3")
while True:
    while True:
        try:
            print("")
            chislo_n = int(input("enter any number: "))
            break
        except ValueError:
            print("only numbers. no dots or other symbols")
    i = chislo_n + 1
    while i != 0:
        i = i - 1
        i2 = chislo_n
        stroka = ""
        for sym in range(i, chislo_n):
            stroka = stroka + str(i2)
            i2 = int(i2) - 1
        print(stroka)                
    
