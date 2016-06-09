while True:
    while True:
        try:
             a = int(input("insert a: "))
             b = int(input("insert b: "))
             c = int(input("insert c: "))
             break
        except ValueError:
             print("sorry. only numbers.")
             
    if  a+b == c:
        print("1. a + b = c! yeah!")
    else:
        print("1. sorry. a + b ≠ c.")

    if a*c+b == 0:
        print("4. ac + b = 0! yeah!")
    else:
        print("4. sorry. ac + b ≠ 0")
    if input("input 'yes' to insert other numbers ") != "yes":
            break
